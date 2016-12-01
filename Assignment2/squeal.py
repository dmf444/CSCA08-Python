from Assignment2.reading import *
from Assignment2.database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results

# Constants for splitting the SELECT COMMAND
COLUMN_COMMAND_LOCATION = 1
TABLE_COMMAND_LOCATION = 3
WHERE_LOCATION = 4
CONTENT_COMMAND_LOCATION = 5


def run_query(database, query):
    """ (Database, str) -> Table
    Function takes a database and a properly formatted sql query and retruns a
    table with the requested information.
    REQ: query must be a properly formatted query.
    REQ: database must be a non-empty database with the requested tables.
    """
    # Split the query on spaces
    commands = query.split(" ")
    # ASSUME: proper format for query
    # Create a table with all of the required tables cartesian planed
    query_table = create_new_tables(database, commands[TABLE_COMMAND_LOCATION])
    # If there is a "where" command
    if(len(commands) > WHERE_LOCATION):
        # Check if there are more than 5 splits. This may occur if a
        # hardcoded value has a space in it, ex. 'St. Lucia'.
        if(len(commands) > CONTENT_COMMAND_LOCATION):
            # If there are extra splits, start with the first split after
            # the where command and parse them all back together
            command = commands[CONTENT_COMMAND_LOCATION]
            # Because we start at the 5th index, loop from that + 1
            for i in range(CONTENT_COMMAND_LOCATION + 1, len(commands)):
                # Make sure to include the spaces back into the parsed text
                command += " " + commands[i]
        else:
            # Otherwise, everything was in one nice string, just use that
            command = commands[CONTENT_COMMAND_LOCATION]
        # Create a new table, following the WHERE parameters
        query_table = filter_table(query_table, command)
    # Create a new table with the requested columns
    new_table = select_columns(query_table, commands[COLUMN_COMMAND_LOCATION])
    # Return the tables
    return new_table


def select_columns(table, commands):
    """ (Table, list [str]) -> Table
    Function takes a table and a comma separated string of column names and
    returns a new table containing only those select columns. commands can also
    be '*' if user wants all columns.
    REQ: table must not be empty
    REQ: commands != '', commands must be separated by commas
    """
    # If user wants all tables
    if(commands == "*"):
        # Return the input table
        ret_table = table
    else:
        # If the commands are not *, assume they are csv
        # Create a blank returning table
        ret_table = Table()
        # If there are more than one columns
        if(commands.find(",") > 0):
            # Split the column names into a list
            column_names = commands.split(",")
            # Loop through all column names
            for column_name in column_names:
                # Get the column from the original table
                column = table.get_column(column_name)
                # Add it to the new returning table
                ret_table.add_column(column_name, column)
        # There is only one column to select
        else:
            # Get the column from the given table, add it to the new table
            column = table.get_column(commands)
            ret_table.add_column(commands, column)
    # Return the new table
    return ret_table


def filter_table(table, filter_commands):
    """ (Table, str) -> Table
    Function takes a table and a string of comma separated where clauses.
    Function processes' all the where clauses and returns a valid table that
    satisfies the where clauses.
    REQ: filter_commands != ''
    REQ: table cannot be empty
    """
    # If there are commas in the given command
    if(filter_commands.find(",") > 0):
        # Split the commands at the commas and store them into an array
        commands = filter_commands.split(",")
        # Create a return table, default it's value to input table, allowing
        #  for easy repetition of commands
        ret_table = table
        # Loop through all commands
        while(len(commands) > 0):
            # Remove the last command
            command = commands.pop()
            # Process the command, store the table into the return table
            ret_table = process_command(ret_table, command)
    # This function was called with only one command
    else:
        # Process the command, store the results into the return table
        ret_table = process_command(table, filter_commands)
    return ret_table


def process_command(table, command):
    """ (Table, str) -> Table
    Function takes in a table and a command, process the command (either
    greater than OR equal command) and returns a new table that adhears to
    the commands.
    REQ: command must be a str with: column_name (> or =) (value or 'value')
    REQ: Table must be a valid table containing the column specified by
         column name in the command
    """
    # If command is equality
    if(command.find("=") > 0):
        # Split the command at the equal sign
        cmds = command.split("=")
        # Get the column name from the command
        column_name = cmds[0]
        # Get the value from the command
        value = cmds[1]
        # If the command is a hard coded value
        if(command.find("'") > 0):
            # Strip the quotation marks
            clean_val = value.replace("'", "")
            # Call the helper function, let it know that input is an equality-E
            ret_table = hardcoded_processor(table, column_name, clean_val, "E")
        else:
            # Otherwise, this is a column, call the column processor,
            # and tell it that the input is an equality - 'E'
            ret_table = column_processor(table, column_name, value, "E")
    # Else assume command is greater than
    else:
        # Split at the > symbol
        cmds = command.split(">")
        # Get the column name from the first index
        column_name = cmds[0]
        # Get the column value from the second index
        value = cmds[1]
        # If the command is a hard coded value (checked by containing '')
        if(command.find("'") > 0):
            # Strip the quotation marks
            clean_val = value.replace("'", "")
            # Call the helper function, let it know that input is greater
            # than- 'G'
            ret_table = hardcoded_processor(table, column_name, clean_val, "G")
        # Otherwise, this is a column, call the column processor
        else:
            # tell it that the input is a greater than comparison - 'G'
            ret_table = column_processor(table, column_name, value, "G")
    # Finally return the processed table
    return ret_table


def hardcoded_processor(table, column_name, value, mode):
    """ (Table, str, str, str) -> Table
    Function takes in a valid table, column_name and comparison value,
    and will process the where command for a hard coded value. Returns a
    table with all valid rows after the where command is completed.
    REQ: column_name must be in the table, cannot be ''.
    REQ: value must be a string or an int
    REQ: mode must be 'G' or 'E'
    """
    # From the table, get the column, given by column_name
    column = table.get_column(column_name)
    # Create a default index of 0 and new table
    index = 0
    new_table = Table()
    # Get the old table's keys
    old_table_keys = table.get_keys_as_list()
    # use these keys for the new return table
    new_table.add_column_titles_to_table(old_table_keys)
    # Loop through the length of the specified column
    while(index < len(column)):
        # Get the field at the index of the loop
        field = column[index]
        # Get the comparative value, given from function
        comp_val = value
        # Try to convert both values to a float
        field = attempt_to_make_float(field)
        comp_val = attempt_to_make_float(comp_val)
        # Assuming that the fields are equal AND the mode is an equality
        # check OR the first is greater than the second AND its a greater
        # than check
        if((field == comp_val and mode == 'E') or (field > comp_val and
                                                   mode == 'G')):
            # Get the row at that index
            row = table.get_row_at_index(index)
            # Insert the row into the new table
            new_table.add_row(old_table_keys, row)
        # Increment the counter
        index += 1
    # Return the final table
    return new_table


def attempt_to_make_float(value):
    """ (str) -> str/float
    Takes in a value and attempts convert it to a float. If the value cannot be
    converted, return the original string value.
    REQ: value must not be ''
    >>> attempt_to_make_float('4.3')
    4.3
    >>> attempt_to_make_float('BIGNINGN')
    'BIGNINGN'
    >>> attempt_to_make_float('4545454545')
    4545454545
    >>> attempt_to_make_float('hello334')
    'hello334'
    """
    try:
        new_value = float(value)
    except:
        new_value = value
    return new_value


def column_processor(table, column1_name, column2_name, mode):
    """ (Table, str, str, str) -> Table
    Function takes in a valid table, column_name and column2_name,
    and will process the where command for a column value. Returns a
    table with all valid rows after the where command is completed.
    REQ: column_name must be in the table, cannot be ''.
    REQ: column2_name must be a in the table, cannot be ''.
    REQ: mode must be 'G' or 'E'.
    """
    # Get the values for the first two columns
    column_1 = table.get_column(column1_name)
    column_2 = table.get_column(column2_name)
    # Create an index and empty table
    index = 0
    new_table = Table()
    # Get the keys from the input table
    old_table_keys = table.get_keys_as_list()
    # Store the column names from the input table into the return table
    new_table.add_column_titles_to_table(old_table_keys)
    # While there are still values in the column
    while(index < len(column_1)):
        # Get the fields from the two columns at the index
        field_1 = column_1[index]
        field_2 = column_2[index]
        # Try and convert them to floats for more accurate comparisons
        field_1 = attempt_to_make_float(field_1)
        field_2 = attempt_to_make_float(field_2)
        # Assuming that the fields are equal AND the mode is an equality
        # check OR the first is greater than the second AND its a greater
        # than check
        if((field_1 == field_2 and mode == 'E') or (field_1 > field_2 and
                                                    mode == 'G')):
            # Get the row at that index
            row = table.get_row_at_index(index)
            # Insert the row into the new table
            new_table.add_row(old_table_keys, row)
        # Increment the counter
        index += 1
    # Return the final table
    return new_table


def cartesian_product(table_1, table_2):
    """ (Table, Table) -> Table
    Function takes in table_1 and table_2, and creates a cartesian product
    of the two tables. This means that every row in table_1 is paired with
    every row from table_2. Normal amount of rows for a table returned from
    this function would be table_1.num_rows() * table_2.num_rows(). Function
    will return a table with the amalgamation of all the rows.
    REQ: table_1 be a valid, non-empty table
    REQ: table_2 be a valid, non-empty table
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
            crossed_table.add_row(crossed_table_keys, new_row)
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
    REQ: database must be a non-empty database containing all tables in
         list_of_table_names
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
    # Read database in current DIR
    database = read_database()
    # Set flag to exit on
    entered_space = False
    # Continuous loop until flag is unset
    while(not entered_space):
        # Get the query from the user
        query = input("Enter a SQuEaL query, or a blank line to exit:")
        # If the query is not a space
        if(not(query == "")):
            # Run the query through the run_query function
            table = run_query(database, query)
            # print the resulting table
            table.print_csv()
        # Otherwise, a blank line was entered
        else:
            # Set the flag to true, exit the loop
            entered_space = True
