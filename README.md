# DriverVulnCheck

## Overview
DriverVulnCheck is a Python tool that takes the output from Bruteratel's `drivers` command and checks it against known vulnerabilities listed on loldrivers.io. This tool helps users identify potentially vulnerable drivers installed on their systems.

## Features
- Extracts driver names from a specified input file.
- Checks extracted driver names against a database of known vulnerable drivers.
- Provides detailed output for any matches found, including categories and resources for further investigation.
- Supports debug mode for verbose output.

## Requirements
- Python 3.x
- Required Python packages:
  - `argparse`
  - `pandas`
  - `requests`
  - `colorama`

You can install the required packages using pip:

```bash
pip install pandas requests colorama
```

## Usage
To use DriverVulnCheck, run the following command in your terminal:

```bash
python drivervulncheck.py -i <input_file> [--debug] [--nc]
```

## Parameters
- `-i`, `--input`: (Required) Path to the input text file containing driver information.
- `--debug`: (Optional) Enable debug output for detailed processing information.
- `--nc`: (Optional) Disable colored output.

## Example
To check a file named `drivers_output.txt` for vulnerabilities, you would run:

```bash
python drivervulncheck.py -i drivers_output.txt
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
- The Bruteratel team for their `drivers` command.
- The loldrivers.io team for their database of known vulnerable drivers.
- The Python community for their support and contributions.

## Contact
For support or questions, please reach out via Twitter: [@vysecurity](https://twitter.com/vysecurity).

## Badges
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)
