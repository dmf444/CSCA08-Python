# Functions for reading tables and databases

import glob
from Assignment2.database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
FILE_LIST = glob.glob('*.csv')


# Write the read_table and read_database functions below
def read_table(file_name):
    """ (str) -> Table
    This function takes in a file_name, reads the file and creates a table with
    all the valid information from the file. This function will return a table
    of all the data.
    REQ: file_name must be a valid .csv file, formated with commas between
    every new entry, new lines for each entry, and the first line containing
    the table keys.
    """
    # Open the file in read mode, read all the lines, close the file
    open_file = open(file_name, 'r')
    all_lines = open_file.readlines()
    open_file.close()

    # Initialize a table
    table = Table()
    # Get the key values, add them to the dictionary
    key_line = all_lines.pop(0)
    key_line = key_line.replace("\n", "")
    keys = key_line.split(",")
    table.add_column_titles_to_table(keys)
    # Loop through all text lines
    for line in all_lines:
        # Check if the line is blank
        if(not(line == "")):
            # Remove any newline charaters
            line = line.replace("\n", "")
            # Split at the commas
            values = line.split(",")
            clean_values = []
            for value in values:
                value = value.lstrip()
                clean_values.append(value)
            # Add the builtin dictionary to the table
            table.add_row_to_table(keys, clean_values)
    return table


def read_database():
    """ () -> Database
    Reads all .csv files in the same directory and creates a database. Returns
    a database of the .csv files.
    REQ: all files in the directory must be valid .csv files.
    """
    # Create an empty database
    database = Database()
    # Loop through every file in the global filelist
    for file in FILE_LIST:
        # Create a table from the file
        table = read_table(file)
        # Find the index of the '.', in order to split the name
        period_index = file.find('.')
        # Get the name of the file, use it as the table name
        table_name = file[0:period_index]
        # Add the table to the database
        database.add_table_to_database(table_name, table)
    return database


if(__name__ == "__main__"):
    table = read_table("csv_files/books.csv")
    table.print_csv()
    base = read_database()
    print(base)