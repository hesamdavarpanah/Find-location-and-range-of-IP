# Find Location and Range of IP

This repository contains a simple Python script that allows users to find the location and range of an IP address. This can be useful for various purposes such as tracking the location of a website visitor or identifying potential security threats.

## How to Use

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the required packages by running `pip install -r requirements.txt` in your terminal.
4. Create a files directory and put the [IP2LOCATION-LITE-ASN.CSV](https://lite.ip2location.com/database-asn?lang=en_US) on this.
5. Run the script by typing `python main.py` in your terminal.
6. The script will output the location and range of the given IP address on MongoDB.

## Technologies Used

- Python
- [ipinfo](https://github.com/ipinfo/python) library for retrieving IP information
- [ipwhois](https://github.com/secynic/ipwhois) library for retrieving WHOIS information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute to this project by creating pull requests or reporting any issues you encounter.

Thank you for using our script!

![Find location and range of IP graph](./IP2Location.png)
