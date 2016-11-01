
def function_names(open_file_handler):
    '''
    This function takes in an open_file_handler (python file) and will scan
    though it to find function names within the file.
    :param open_file_handler: io.TextIOWrapper, a file handler in the read mode
    :return: list of strings
    '''
    # Two lists, one of file text, other (empty) with found fn names
    text_list = open_file_handler.readlines()
    found_func_names = []
    # Iterate through list, if def is found, strip it, split string at (
    for text in text_list:
        if ("def " in text):
            text = text.lstrip("def ")
            func_name = text.rsplit("(")
            # add the name to the found fn list
            found_func_names.append(func_name[0])
    # Return the list of found functions
    return found_func_names


def justified(open_file_handler):
    '''
    Function takes in an open_file_handler, and will scan through the files to
    see if the entire file is left-justified. If the line starts with a space,
    this function will return False. Otherwise, it will return True.
    :param open_file_handler: io.TextIOWrapper, opened in Read mode
    :return: Boolean
    '''
    flag = True
    # Read the initial line
    text = open_file_handler.readline()
    # Iterate through the lines in the text, if flag is false, stop
    while(flag and text):
        # If we find a space at the begining of the word, set the flag to false
        if(text.startswith(" ")):
            flag = False
        # Read the next line for the loop
        text = open_file_handler.readline()
    return flag
