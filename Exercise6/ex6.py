def copy_me(list_in):
    '''
    Fuction that copies list_in and edits the values according to a set of rules. Returns a copy of the original list
    with the following changes: Strings are all uppercase, numbers are increased by 1, booleans are negated and list are
    replaced with 'List'.
    :param list_in: any list.
    :return: list.
    >>> copy_me([1, 3.4, "hello", [1,2,3], False])
    [2, 4.4, 'HELLO', 'List', True]
    >>> copy_me([0.4, "merpetty merp", (1,2,3), True])
    [1.4, 'MERPETTY MERP', (1, 2, 3), False]
    '''
    # Copy the list
    edit_list = list_in[:]
    # Loop through all indexes of the list
    for count in range(0, len(edit_list)):
        selection = edit_list[count]
        # Switch through all list, change based on types
        # Strings are uppercase
        # Floats/Ints are added to
        # Bools are notted
        # Everything else is left alone
        if(type(selection) == str):
            new_var = selection.upper()
        elif(type(selection) == float or type(selection) == int):
            new_var = selection + 1
        elif(type(selection) == bool):
            new_var = not selection
        elif(type(selection) == list):
            new_var = "List"
        else:
            new_var = selection
        # Set changed var to new var
        edit_list[count] = new_var
    return edit_list


def mutate_me(list_in):
    '''
    Fuction that edits list_in and changes the values according to a set of rules. Returns none but makes the following
    changes to the list: Strings are all uppercase, numbers are increased by 1, booleans are negated and list are
    replaced with 'List'.
    :param list_in: any list.
    :return: list.
    >>> mutate_me([1, 3.4, "hello", [1,2,3], False])
    [2, 4.4, 'HELLO', 'List', True]
    >>> mutate_me([0.4, "merpetty merp", (1,2,3), True])
    [1.4, 'MERPETTY MERP', (1, 2, 3), False]
    '''
    # Copy the list
    # Loop through all indexes of the list
    for count in range(0, len(list_in)):
        selection = list_in[count]
        # Switch through all list, change based on types
        # Strings are uppercase
        # Floats/Ints are added to
        # Bools are notted
        # Everything else is left alone
        if(type(selection) == str):
            new_var = selection.upper()
        elif(type(selection) == float or type(selection) == int):
            new_var = selection + 1
        elif(type(selection) == bool):
            new_var = not selection
        elif(type(selection) == list):
            new_var = "List"
        else:
            new_var = selection
        # Set changed var to new var
        list_in[count] = new_var
