def greeting(person_name):
    return "Hello " + person_name + " how are you today?"


def mutate_list(list_in):
    for i in range(len(list_in)):
        to_mod = list_in[i]
        if(isinstance(to_mod, bool)):
            changed_var = not to_mod
        elif(isinstance(to_mod, int)):
            changed_var = 2 * to_mod
        elif(isinstance(to_mod, str)):
            changed_var = to_mod[1:-1]
        else:
            changed_var = to_mod
        list_in[i] = changed_var
    list_in[0] = "Hello"


def merge_dicts(dictionary_1: dict, dictionary_2: dict):
    '''
    Merges two seperated dictionaries into one. Dictionaries must be of type
    {str: [int]}. If there is a shared key, the value of the second dict is
    appended to the first dictionary's list.
    :param dictionary_1: {str: [int]}, cannot be null
    :param dictionary_2: {str: [int]}, cannot be null
    :return: {str: [int]}
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'c': [5, 6, 7], 'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'd': [10, 11, 12]}
    >>> d3 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d4 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d4, d3)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    '''
    ret_dict = dictionary_1
    dict_2_key = dictionary_2.keys()
    for key in dict_2_key:
        dict_2_val = dictionary_2[key]
        if key in ret_dict:
            value = ret_dict[key]
            ret_dict[key] = value + dict_2_val
        else:
            ret_dict[key] = dict_2_val
    return ret_dict
