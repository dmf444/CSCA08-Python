class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self):
        '''
        Initialization parameters of only self, used to create an empty
        dictionary.
        '''
        self._table_dict = dict()

    def add_dict(self, new_dict):
        """ (Table, dict of {str: list of str}) -> NoneType
        Makes a copy of the dictionary and adds it to the internally stored
        dictionary

        """
        keys = new_dict.keys()
        for key in keys:
            dict_value = new_dict[key]
            self._table_dict[key] = dict_value

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

    def num_rows(self):
        if(len(list(self._table_dict.items())) > 0):
            row_num = len(list(self._table_dict.items())[0])
        else:
            row_num = 0
        return row_num

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
