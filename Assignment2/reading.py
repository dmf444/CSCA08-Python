# Functions for reading tables and databases

import glob
from database import *


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
            # Iterate through all the values from the split line
            for value in values:
                # Clear out any white spaces (to the left)
                value = value.lstrip()
                # Add value to a new list
                clean_values.append(value)
            # Add the builtin dictionary to the table
            table.add_row(keys, clean_values)
    return table


def read_database():
    """ () -> Database
    Reads all .csv files in the same directory and creates a database. Returns
    a database of the .csv files.
    REQ: all files in the directory must be valid .csv files.
    REQ: .csv files must follow the proper formatting
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
