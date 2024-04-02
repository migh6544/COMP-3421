## START:


# Import to handle MySQL connections
import mysql.connector
# Import to handle CSV file operations
import csv
# Import to handle file path operations
import os
# Import to handle zip file operations
import zipfile
# Import to securely input the password
import getpass


def get_database_connection_params():
    """
    Prompts the user to input database connection parameters and returns a dictionary containing these parameters.

    Returns:
        dict: A dictionary with keys 'user', 'passwd', 'database', 'host', each containing respective connection parameters.
    """

    # Display welcome message and instructions
    print("\n\n\n*** --{ Welcome to the Database Data-Export Portal! }-- ***\n\n")
    # Prompt the user for their MySQL username
    user = input("Please enter your MySQL username: ")
    # Securely prompt the user for their MySQL password
    passwd = getpass.getpass("Please enter your MySQL password: ")
    # Prompt the user for the database name they wish to use
    database = input("Please enter the database you wish to use: ")
   # Define the host as localhost, which is a constant in this context
    host = '127.0.0.1'
    # Return the database connection parameters as a dictionary
    return {'user': user, 'passwd': passwd, 'database': database, 'host': host}

def export_table_to_csv(database_connection_params):
    """
    Connects to a MySQL database using provided connection parameters, lists available tables,
    and allows the user to select a table to export to a CSV file or to export all tables to a ZIP file.

    Parameters:
        database_connection_params (dict): Database connection parameters including user, password, database, and host.
    """

    # Establish connection to the MySQL database using provided parameters
    mydb = mysql.connector.connect(
        user = database_connection_params['user'],
        passwd = database_connection_params['passwd'],
        database = database_connection_params['database'],
        host = database_connection_params['host'],
        # Enable loading data from local files if necessary
        allow_local_infile = '1'
    )

    # Create a cursor object using the connection
    myc = mydb.cursor()

    # Explicitly selecting a database (might be redundant or necessary based on context)
    myc.execute("USE HR")

    while True:
        # Display instructions and available tables to the user
        print("\nHere are the tables available for export:\n")
        myc.execute("SHOW TABLES")
        # Fetch all table names from the cursor and display them
        tables = [x[0] for x in myc.fetchall()]
        for table_name in tables:
            print(f"> {table_name}")

        # Prompt user for action: export a table, export all tables, or exit
        userInput = input("\n\nINSTRUCTIONS:\nType the name of the table you would like to export, type 'All' to export all available tables, or type 'Exit' to quit.\nWhat would you like to do?\n")
        # Check if user wants to exit the loop
        if userInput.lower() == 'exit':
            break

        # If user wants to export all tables
        if userInput.lower() == 'all':
            # Filename for the zip file is based on the database name
            zip_filename = f"{database_connection_params['database']}_Database_Tables.zip"
            # Create a ZIP file and export each table as a CSV into this ZIP
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for tableName in tables:
                    # Export each table to CSV
                    csv_file = export_to_csv(myc, tableName)
                    # Add the CSV file to ZIP
                    zipf.write(csv_file, os.path.basename(csv_file))
                    # Remove the CSV file after adding it to ZIP
                    os.remove(csv_file)
            print(f"All tables have been successfully exported into '{zip_filename}'.")
            continue

        # Look for the user-specified table in the list of tables
        tableName = next((table for table in tables if table.lower() == userInput.lower()), None)
        # If the specified table is not found, inform the user and continue the loop
        if tableName is None:
            print("Table not found. Please ensure you've entered the correct table name.")
            continue

        # If a specific table name is provided, export that table to CSV
        export_to_csv(myc, tableName)

def export_to_csv(myc, tableName):
    """
    Fetch data from the specified table and export it to a CSV file. Returns the path of the created CSV file.

    Parameters:
    myc: The MySQL cursor.
    tableName (str): The exact case-sensitive name of the table to be exported.
    """

    # SQL query to select all data from the specified table
    query = f"SELECT * FROM `{tableName}`"
    # Execute the query using the cursor
    myc.execute(query)
    # Fetch all rows from the query result
    rows = myc.fetchall()
    # Extract column headers from the cursor description
    columns = [i[0] for i in myc.description]

    # Define the filename for the CSV file
    csv_file = f"{tableName}.csv"
    # Open a new CSV file and write the data
    with open(csv_file, mode = 'w', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        # Write the column headers as the first row
        writer.writerow(columns)
        # Write the data rows
        writer.writerows(rows)

    # Inform the user of successful export
    print(f"Table '{tableName}' has been successfully exported to '{csv_file}'.")
    # Return the path to the created CSV file
    return csv_file

def main():
    """
    The main entry point of the application when run as a script.
    """

    # Obtain database connection parameters from the user
    database_connection_params = get_database_connection_params()
    # Export selected table(s) to CSV based on user input and connection parameters
    export_table_to_csv(database_connection_params)


# Check if the script is being run directly (as opposed to being imported) and call main
if __name__ == "__main__":
    main()


## END.