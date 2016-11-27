from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def run_query(database, query):
    """ (Database, str) -> Table
    Function takes a database and a properly formatted sql query and retruns a
    table with the requested information.
    REQ: query must be a properly formatted query.
    REQ: database must be a non-empty database with the requested tables.
    """
    commands = query.split(" ")
    if(commands[0] == "SELECT"):
        create_new_tables(database, commands[1])


def create_new_tables(database, tables):
    """ (Database, str) -> Table
    Function takes a database and a string of tables, separated by commas.
    Function then comuptes the cartesian product of all given tables,
    and returns the table of tables.
    REQ: table must be a comma separated string of valid tables
    REQ: database must be a valid, non-empty database.
    """

    if(tables.find(",") > 0):
        to_product = tables.split(",")
        table_array = create_array_of_tables(database, to_product)
        while(len(table_array) > 1):
            table_1 = table_array.pop(0)
            table_2 = table_array.pop(1)
            cartisian_table = cartesian_product(table_1, table_2)
            table_array.insert(0, cartisian_table)
        ret_table =
    else:
        ret_table = database.get_table(tables)
    return ret_table


def create_array_of_tables(database, list_of_table_names):
    """(Database, list [str]) -> list [Tables]
    """
    tabels = []
    for table_names in list_of_table_names:
        tabel = database.get_table(table_names)
        tabels.append(tabel)
    return tabels


if(__name__ == "__main__"):
    database = read_database()
    query = input("Enter a SQuEaL query, or a blank line to exit:")
    tablet = create_new_tables(database, "csv_files\olympics-results,"
                                         "csv_files\olympics-locations")
    tablet.print_csv()

