# Database Data-Export Tool

This Python script provides a user-friendly interface to export data from MySQL database tables to CSV files. It allows users to securely connect to their MySQL database, select specific tables for export, or export all tables at once into a ZIP file. This tool is designed to simplify the process of data extraction for analysis, backup, or migration purposes.


## Features

- **Secure Connection:** Prompts for database credentials securely, ensuring password protection.
- **Table Selection:** Offers a list of available tables within the database for selective data export.
- **Bulk Export:** Allows exporting all tables into a ZIP file for comprehensive backup or analysis.
- **User-Friendly Interface:** Simple command-line prompts guide the user through the process, making it accessible for non-technical users.

## Requirements

Before running this script, ensure you have the following installed:
- Python 3.x
- `mysql.connector` Python package
- Other Python packages: `csv`, `os`, `zipfile`, `getpass`


## Setup

#### Install MySQL Connector:
If not already installed, you can install the `mysql.connector` package using pip:

    pip install mysql-connector-python


## Usage

To use this tool, follow these steps:

1. **Navigate to the Script Directory:**
Open a terminal or command prompt and navigate to the directory where the script is located.

2. **Run the Script:**
Execute the script by running:

    python Python_Connector.py

3. **Enter Database Credentials:**
Follow the on-screen prompts to enter your MySQL username, password, and the database name you wish to export data from. The host is predefined as `localhost`.

4. **Select Tables for Export:**
The script will display a list of available tables. You can choose to export a specific table, all tables, or exit the application.

5. **Retrieve Exported Files:**
The exported CSV file(s) will be saved in the same directory as the script. If you chose to export all tables, a ZIP file containing all CSV files will be created.


## Note

This script assumes that the MySQL database is hosted on `localhost`. If you need to connect to a database hosted on a different server, you will need to modify the `host` parameter within the script accordingly.