import argparse
import re
import pandas as pd
import requests
from io import StringIO  # Correct import for StringIO
import re
from colorama import init, Fore, Style

def extract_driver_names(input_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Regex to find all module names
    module_names = re.findall(r'- Module Name\s+:\s+(.*?)(?=\n)', content)
    
    # Extract only the driver file names
    driver_names = [name.split('\\')[-1] for name in module_names]
    
    return driver_names

def main():
    parser = argparse.ArgumentParser(description='Extract driver names from input file and check against known vulnerabilities.')
    parser.add_argument('-i', '--input', required=True, help='Input text file containing driver information')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--nc', action='store_true', help='No color output')
    args = parser.parse_args()

    # Initialize colorama
    if not args.nc:
        init(autoreset=True)

    driver_names = extract_driver_names(args.input)
    
    # Output the driver names
    #for name in driver_names:
    #    print(name)
    
    # Read the CSV file from the URL
    url = "https://www.loldrivers.io/api/drivers.csv"
    response = requests.get(url)
    csv_data = response.content.decode('utf-8')
    
    # Load the CSV data into a DataFrame
    df = pd.read_csv(StringIO(csv_data))  # Use StringIO directly

    # Convert 'Tags' to string type for comparison and strip whitespace
    df['Tags'] = df['Tags'].astype(str).str.strip()

    # Extract driver names from the input file
    driver_names = extract_driver_names(args.input)  # Ensure this is called to get the driver names

    # Define consistent blue color
    blue_color = Fore.BLUE

    # Check for existing drivers (case-insensitive)
    for driver in driver_names:
        driver_cleaned = driver.strip().lower()  # Clean and lower case the driver name
        
        if args.debug:
            print(f"{blue_color}Checking driver: {driver_cleaned}{Style.RESET_ALL}")
        
        # Check for partial matches in the Tags
        found = False
        for index, tags in df['Tags'].items():  # Use items() instead of iteritems()
            # Split the tags by comma and strip whitespace
            tag_list = [tag.strip().lower() for tag in tags.split(',')]
            if driver_cleaned in tag_list:
                # Print the relevant columns for the matched item
                print(f"{blue_color}[!] Match found for {Fore.RED}{driver}{Style.RESET_ALL}:")
                print(f"{blue_color}Category: {df.at[index, 'Category']}{Style.RESET_ALL}")
                print(f"{blue_color}Resources:")
                for resource in eval(df.at[index, 'Resources']):  # Assuming Resources is a list in string format
                    print(f"    {Fore.GREEN}{resource}{Style.RESET_ALL}")
                print(f"{blue_color}MD5:{Style.RESET_ALL} {Fore.GREEN}{df.at[index, 'KnownVulnerableSamples_MD5']}{Style.RESET_ALL}")
                print(f"{blue_color}SHA1:{Style.RESET_ALL} {Fore.GREEN}{df.at[index, 'KnownVulnerableSamples_SHA1']}{Style.RESET_ALL}")
                print(f"{blue_color}SHA256:{Style.RESET_ALL} {Fore.GREEN}{df.at[index, 'KnownVulnerableSamples_SHA256']}{Style.RESET_ALL}")
                print("Please manually verify the hash against the driver.")
                print()  # Add additional spacing
                found = True
                break  # Exit the loop once a match is found
        
        if args.debug and not found:
            print(f"{Fore.RED}{driver_cleaned} not found in Tags.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
