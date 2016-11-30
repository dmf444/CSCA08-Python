class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self):
        '''
        Initialization parameters of only self, used to create an empty
        dictionary.
        '''
        self._table_dict = dict()

    def add_column_titles_to_table(self, key_list):
        """ (Table, list [str]) -> NoneType
        Function adds a key_list of strings as colunm names to the table.
        Returns none.
        REQ: key_list must only contain strings and not be empty
        REQ: strings in key_list must be unique
        """
        # Loop through the keys
        for key in key_list:
            # Add key with blank list to dictionary
            self._table_dict[key] = []

    def add_row(self, key_list, value_list):
        """ (Table, list [str], list [str]) -> NoneType
        Function takes in a key_list with positions corresponding in value_list
        and adds each value to the key in the table. Returns none.
        REQ: key_list and value_list must have the same length
        REQ: The values in value_list must correspond to the key at the same
             index in key_list
        """
        # Loop through the length of key_list
        for count in range(len(key_list)):
            # Get the key
            col_name = key_list[count]
            # Get the current value of the key
            current_dict_values = self._table_dict[col_name]
            # Append the new value (from value_list) to the key
            current_dict_values.append(value_list[count])

    def get_column(self, column_name):
        """(Table, str) -> List [str]
        Function takes a column name and returns a list containing all items in
        that colunm.
        REQ: column_name must be a valid column in the table
        """
        # Get the column stored in the dictionary
        column = self._table_dict[column_name]
        return column

    def add_column(self, title, value_list):
        """(Table, str, list[str]) -> NoneType
        """
        self._table_dict[title] = value_list

    def num_rows(self):
        keys = self.get_keys_as_list()
        if(len(keys) > 0):
            first_key = keys[0]
            list = self._table_dict[first_key]
            row_num = len(list)
        else:
            row_num = 0
        return row_num

    def get_row_at_index(self, index):
        '''(Table, index) -> list [str]
        Function takes in an index, finds the row required and returns an array
        with the data of that row.
        REQ: 0 < index < self.num_rows()
        '''
        columns = self.get_keys_as_list()
        col = []
        for column in columns:
            col.append(self._table_dict[column][index])
        return col

    def get_keys_as_list(self):
        key_list = list(self._table_dict.keys())
        return key_list

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self._table_dict = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._table_dict

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))


class Database():
    '''A class to represent a SQuEaL database'''

    def __init__(self):
        ''' (Database) -> NoneType
        Initialization function, creates an empty table.
        '''
        self._database = dict()

    def __str__(self):
        """(Database) -> String
        Overrides the str function for easy printing and debugging
        """
        data_return = "Database contains:\n"
        data_return += str(self._database.keys())
        return data_return

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self._database = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._database

    def add_table_to_database(self, table_name, table):
        """ (Database, str, Table) -> NoneType
        This function adds a table to the database. This function will
        over-wright any other tables in the database.
        REQ: table_name must not be empty
        REQ: table must be an instance of database.Table
        """
        self._database[table_name] = table

    def get_table(self, table_name):
        """ (Database, str) -> Table
        Takes in a table_name and returns a stored table.
        REQ: table_name must be in the table.
        """
        return self._database[table_name]
