from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results
COLUMN_COMMAND_LOCATION = 1
TABLE_COMMAND_LOCATION = 3
CONTENT_COMMAND_LOCATION = 5


def run_query(database, query):
    """ (Database, str) -> Table
    Function takes a database and a properly formatted sql query and retruns a
    table with the requested information.
    REQ: query must be a properly formatted query.
    REQ: database must be a non-empty database with the requested tables.
    """
    commands = query.split(" ")
    query_table = create_new_tables(database, commands[TABLE_COMMAND_LOCATION])
    if(len(commands) > 4):
        query_table = filter_table(query_table,
                                   commands[CONTENT_COMMAND_LOCATION])
    new_table = select_columns(query_table, commands[COLUMN_COMMAND_LOCATION])
    return new_table


def select_columns(table, commands):
    if(commands == "*"):
        ret_table = table
    else:
        ret_table = Table()
        if(commands.find(",") > 0):
            column_names = commands.split(",")
            for column_name in column_names:
                column = table.get_column(column_name)
                ret_table.add_column(column_name, column)
        else:
            column = table.get_column(commands)
            ret_table.add_column(commands, column)
    return ret_table


def filter_table(table, filter_commands):
    pass


def cartesian_product(table_1, table_2):
    """ (Table, Table) -> Table
    """
    # Create an empty table to return
    crossed_table = Table()
    # Get the column names from t1 and t2
    t1_keys = table_1.get_keys_as_list()
    t2_keys = table_2.get_keys_as_list()
    # Create a list with the two key sets
    crossed_table_keys = t1_keys + t2_keys
    # Add keys to the new table
    crossed_table.add_column_titles_to_table(crossed_table_keys)
    # Loop through all rows in the first table
    for t1_index in range(table_1.num_rows()):
        # Store the row as a variable
        row_1 = table_1.get_row_at_index(t1_index)
        # Loop through all the rows in the second table
        for t2_index in range(table_2.num_rows()):
            # Store the second table's row
            row_2 = table_2.get_row_at_index(t2_index)
            # Add table1's and table2's current stored row
            new_row = row_1 + row_2
            # Add these values to the new table
            crossed_table.add_row_to_table(crossed_table_keys, new_row)
    return crossed_table


def create_new_tables(database, tables):
    """ (Database, str) -> Table
    Function takes a database and a string of tables, separated by commas.
    Function then computes the cartesian product of all given tables,
    and returns the table of tables.
    REQ: table must be a comma separated string of valid tables
    REQ: database must be a valid, non-empty database.
    """
    # Check if there is more than one table listed in the string
    if(tables.find(",") > 0):
        # If there is:
        # Split the string at commas
        to_product = tables.split(",")
        # Create an array with all the valid tables
        table_array = create_array_of_tables(database, to_product)
        # While there are more than 1 tables in the array
        while(len(table_array) > 1):
            # Remove the first table in the array, store it as table 1
            table_1 = table_array.pop(0)
            # Remove the new first table in the array, store it as table 2
            table_2 = table_array.pop(0)
            # Create a cartesian cross of the two tables
            cartisian_table = cartesian_product(table_1, table_2)
            # Reinsert the cartesian crossed array to the begining of the list
            table_array.insert(0, cartisian_table)
        # Set the return list the the first table in the array
        ret_table = table_array[0]
    else:
        # Get the table from the database
        ret_table = database.get_table(tables)
    return ret_table


def create_array_of_tables(database, list_of_table_names):
    """(Database, list [str]) -> list [Tables]
    Function takes in a list_of_table_names, finds the individual tables in the
    database and adds them to a list. Function will return the list of Tables.
    REQ: list_of_table_names must contain valid table names AND != []
    """
    # Create an empty return list
    tabels = []
    # Loop through all the tables in the given list
    for table_names in list_of_table_names:
        # Get the table from the database, add it to the return list
        tabel = database.get_table(table_names)
        tabels.append(tabel)
    return tabels


if(__name__ == "__main__"):
    database = read_database()
    entered_space = False
    while(not entered_space):
        query = input("Enter a SQuEaL query, or a blank line to exit:")
        if(not(query == "")):
            table = run_query(database, query)
            table.print_csv()
        else:
            entered_space = True
    #tablet = create_new_tables(database, "movies,oscars,whammies")
    #tablet.print_csv()
    #print(tablet.num_rows())

