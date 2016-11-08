def create_dict(open_file_handler):
    """
    This function takes an open file, and creates a dictionary that maps a username to other information on the person.
    :param open_file_handler: io.TextIOWrapper
    :return: dict of {str: [str, str, str, int, str]}, where the list is of order:
    [last name, first name, e-mail, age, gender]
    """
    # Get all the text from the file
    person_details = open_file_handler.readlines()
    # Create an empty dictionary
    person_dictionary = {}
    # iterate every line in the file
    for person in person_details:
        # Remove line seperators, spilt text on spaces
        person = person.replace("\n", "")
        person_info = person.split(" ")
        # Get each field from the standard format of the text file
        username = person_info[0]
        first_name = person_info[1]
        last_name = person_info[2]
        age = person_info[3]
        gender = person_info[4]
        email = person_info[5]
        # Create a list with all the required data
        information_list = [last_name, first_name, email, age, gender]
        # Add the username to the dictionary with the list
        person_dictionary[username] = information_list
    return person_dictionary


def update_field(dictionary, key, field, new_value):
    """
    This function updates a field in the dictionary with the new_value, applied to the given key. Returns a nonetype
    :param dictionary: a dictionary in the format of {str: [str, str, str, int, str]}
    :param key: the string key of the username that needs to be updated
    :param field: string, specific field than needs to be updated, either: 'LAST', 'FIRST', 'EMAIL', 'AGE', 'GENDER'
    :param new_value: the new value to be inputted
    :return: NoneType
    >>> my_dict = {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
    >>> update_field(my_dict, 'sclause', 'AGE', 999)
    >>> my_dict == {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 999, 'M']}
    True
    """
    # Get the key's list
    info_list = dictionary[key]
    # If the user wants to update lastname
    if(field == "LAST"):
        info_list[0] = new_value
    # If the user wants to update First Name
    elif(field == "FIRST"):
        info_list[1] = new_value
    # If the user wants to update Email
    elif(field == "EMAIL"):
        info_list[2] = new_value
    # If the user wants to update Age
    elif(field == "AGE"):
        info_list[3] = new_value
    # If the user wants to update Gender
    elif(field == "GENDER"):
        info_list[4] = new_value


def select(dictionary, type_to_return, type_to_check, value_to_check):
    """
    Given a dictionary, this function will use type_to_check, and look for a specific value_to_check. It will return a
    set of type_to_return.
    :param dictionary:  a dictionary in the format of {str: [str, str, str, int, str]}, dictionary cannot be empty
    :param type_to_return: STRING of data that need to be returned, cannot be null
    :param type_to_check: string of type to check, cannot be null
    :param value_to_check: value to match, cannot be null
    :return: set of type_to_return
    """
    # Simple dictionary for index values
    data_dict = {"LAST": 0, "FIRST": 1, "EMAIL": 2, "AGE": 3, "GENDER": 4}
    # Create an empty set to return
    data_set = set()
    # Loop through all usernames
    for username in dictionary:
        # Grab the data list for each user
        data_list = dictionary[username]
        # Get the value of the type that was requested for comparison
        type = data_list[data_dict[type_to_check]]
        # If the type matches the request one
        if(type == value_to_check):
            # Get the specified return values
            ret_val = data_list[data_dict[type_to_return]]
            # Add it to the set
            data_set.add(ret_val)
    # Return the set
    return data_set
