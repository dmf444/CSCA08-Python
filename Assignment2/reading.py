# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING
FILE_LIST = glob.glob('csv_files/*.csv')


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
    # Create an empty dictionary to hold the values
    holding_dictionary = dict()
    # Get the key values, add them to the dictionary
    key_line = all_lines.pop(0)
    key_line = key_line.replace("\n", "")
    keys = key_line.split(",")
    # Loop through keys, add them to dictionary
    for key in keys:
        holding_dictionary[key] = []
    # Add values to the dictionary
    for line in all_lines:
        line = line.replace("\n", "")
        values = line.split(",")
        for count in range(0, len(values)):
            # Get dictionary key
            dict_key = keys[count]
            # Get holding array
            val_list = holding_dictionary[dict_key]
            # Append new value to list
            val_list.append(values[count])
    # Initialize a table with an empty dict
    table = Table()
    # Add the builtin dictionary to the table
    table.add_dict(holding_dictionary)
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