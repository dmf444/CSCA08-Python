# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                      'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
                      'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                      'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
                      'Z': 25}


def clean_message(message):
    """(str) -> str
    This function takes in a String message and cuts out all spaces, then puts
    everything in uppercase. Returns the new string
    REQ: message != null, message can only contain alphabetic charaters
    >>> clean_message("no body knows the trouble ive seen")
    'NOBODYKNOWSTHETROUBLEIVESEEN'
    >>> clean_message("FHSLR D")
    'FHSLRD'
    >>> clean_message("CSCA 08 is the best F@*$#(% course EVAH!!!!!!")
    'CSCAISTHEBESTFCOURSEEVAH'
    """
    # Replace all spaces in the message with empty strings
    new_message = message.replace(" ", "")
    # Convert the entire message to uppercase, then return
    new_message = new_message.upper()
    if(not new_message.isalpha()):
        newer_message = ""
        for letter in new_message:
            if(letter.isalpha()):
                newer_message += letter
        new_message = newer_message
    return new_message


def encrypt_letter(letter, key_value):
    """(str, int) -> str
    This function takes in a letter, converts it to a number and applies the
    key_value to that number, then returns a letter, corresponding to the newly
    generated number.
    REQ: key_value >= 0 and <= 25
    REQ: letter != '' and letter has one Character
    >>> encrypt_letter('A', 3)
    'D'
    >>> encrypt_letter('Z', 6)
    'F'
    >>> encrypt_letter('W', 30)
    'A'
    """
    # Get the numerical value of the given letter
    letter_key = LETTERS_TO_NUMBERS[letter]
    # Add the letter number to the given key value
    crypt_key = letter_key + key_value
    # Modulus the new number against 26 (or length of dict)
    new_key = crypt_key % len(LETTERS_TO_NUMBERS)
    # Inverse the dictionary, therefore giving numbers from letters
    result = {}
    for next_key in LETTERS_TO_NUMBERS:
        next_value = LETTERS_TO_NUMBERS[next_key]
        result[next_value] = next_key
    # Get the new letter and return it
    new_letter = result[new_key]
    return new_letter


def decrypt_letter(letter, key_value):
    """(str, int) -> str
    This function takes in a letter, converts it to a number and removes the
    key_value from that number, then returns a letter, corresponding to the
    original text of the encrypted message.
    REQ: key_value >= 0 and <= 25
    REQ: letter != '' and letter has one Character
    >>> decrypt_letter('A', 45)
    'H'
    >>> decrypt_letter('Z', 504)
    'P'
    >>> decrypt_letter('H', 5)
    'C'
    """
    # Get the numerical value of the given letter
    letter_key = LETTERS_TO_NUMBERS[letter]
    # Add the letter number to the given key value
    crypt_key = letter_key - key_value
    # Modulus the new number against 26 (or length of dict)
    new_key = crypt_key % len(LETTERS_TO_NUMBERS)
    # Inverse the dictionary of letters to numbers,
    # therefore giving numbers from letters
    result = {}
    for next_key in LETTERS_TO_NUMBERS:
        next_value = LETTERS_TO_NUMBERS[next_key]
        result[next_value] = next_key
    # Get the new letter and return it
    new_letter = result[new_key]
    return new_letter


def swap_cards(card_list, index):
    """ (list, int) -> NoneType
    This function takes a card_list, finds a specific card at an index and
    swaps in with the card next to it. This function treats the card_list as
    circular, if index is the highest number in the list, the card will be
    swapped with the lowest int.
    REQ: list must be a list of integers
    REQ: 0 <= index < len(card_list)
    >>> list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    >>> swap_cards(list1, 4)
    >>> print(list1)
    [1, 2, 3, 4, 6, 5, 7, 8, 9, 0]
    >>> list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    >>> swap_cards(list2, 9)
    >>> print(list2)
    [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    """
    # If the index is an edge case (is the last card)
    if(index == len(card_list) - 1):
        # Make a temporary variable to store the first number,
        #  set the last number to the first number, and vice-versa
        temp_value = card_list[0]
        card_list[0] = card_list[index]
        card_list[index] = temp_value
    else:
        # Get the value above the index, save it to a temp variable.
        # Set index + 1's value to index and index's value to
        # the temp variable
        temp_value = card_list[index + 1]
        card_list[index + 1] = card_list[index]
        card_list[index] = temp_value


def move_joker_1(card_list):
    """ (list of integers) -> NoneType
    This function takes in a card_list, finds the joker value (27) and moves
    it up 1 position.
    REQ: card_list must be a list of integers
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21]
    >>> list1 += [24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_1(list1)
    >>> print(list1)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 27,
     5, 8, 11, 14, 17, 20, 23, 26]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21]
    >>> list2 += [24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 27]
    >>> move_joker_1(list2)
    >>> print(list2)
    [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5,
    8, 11, 14, 17, 20, 23, 26, 1]
    >>> list3 = [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18]
    >>> list3 += [21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1]
    >>> move_joker_1(list3)
    >>> print(list3)
    [4, 27, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5,
    8, 11, 14, 17, 20, 23, 26, 1]
    """
    # Create a flag for exiting the while loop & index for where the joker is
    joker_found = False
    current_index = 0
    # As long as the joker is not found, continue the loop
    while(not joker_found):
        # Get the card at the current index, if it's the joker,
        # set the flag to true, otherwise, add 1 to index
        card = card_list[current_index]
        if(card == JOKER1):
            joker_found = True
        else:
            current_index += 1
    # once the joker has been found, swap it with the card above it
    swap_cards(card_list, current_index)


def move_joker_2(card_list):
    """ (list of integers) -> NoneType
    This function takes in a card_list, finds the second joker value (28)
    and moves it up the list 2 positions. This function treats the dec as
    circular and will move Joker2 back to the begining of the list if it cannot
    move to a higher index.
    REQ: card_list must be a list of integers
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21]
    >>> list1 += [24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_2(list1)
    >>> print(list1)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 18, 21, 24, 27,
     2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18]
    >>> list2 += [21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 28, 26]
    >>> move_joker_2(list2)
    >>> print(list2)
    [28, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2,
     5, 8, 11, 14, 17, 20, 26, 1]
    >>> list3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21]
    >>> list3 += [24, 27, 2, 5, 8, 11, 14, 17, 20, 26, 28]
    >>> move_joker_2(list3)
    >>> print(list3)
    [4, 28, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2,
     5, 8, 11, 14, 17, 20, 26, 1]
    """
    # Create a flag for exiting the while loop & index for where the joker is
    joker_found = False
    current_index = 0
    while(not joker_found):
        # Get the card at the current index, if it's the joker,
        #  set the flag to true, otherwise, add 1 to index
        card = card_list[current_index]
        if(card == JOKER2):
            joker_found = True
        else:
            current_index += 1
    # once the joker has been found, swap it with the card above it,
    #  then again with the card above it
    swap_cards(card_list, current_index)
    swap_cards(card_list, (current_index + 1) % len(card_list))


def triple_cut(card_list):
    ''' (list of integer) -> NoneType
    This function takes a card_list, finds all number above the second joker
    and put them at the bottom of the list. At the same time it takes all
    number below the first joker and puts them at the top of the list. If the
    jokers are on the top or bottom of the list, no numbers are changed.
    REQ: card_list must be a list of integers, cannot be empty
    >>> list3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 9, 12, 15, 18]
    >>> list3 += [21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> triple_cut(list3)
    >>> print(list3)
    [2, 5, 8, 11, 14, 17, 20, 26, 28, 9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10,
    13, 16, 19, 22, 25, 23, 3, 6]
    >>> list2 = [28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18]
    >>> list2 += [21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 27]
    >>> triple_cut(list2)
    >>> print(list2)
    [28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2,
    5, 8, 11, 14, 17, 20, 26, 27]
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> triple_cut(list1)
    >>> print(list1)
    [9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 28, 27, 1, 4, 7, 10,
    13, 16, 19, 22, 25, 23, 3, 6]
    '''
    # Get the index of the two jokers
    joker_1_index = card_list.index(JOKER1)  # card value of 27
    joker_2_index = card_list.index(JOKER2)  # card value of 28
    # Do the cuts based on which joker is first in the list
    if(joker_1_index > joker_2_index):
        # Cut the card list into three parts, representing all cards from 0 to
        #  JOKER2, JOKER2 to JOKER1 and JOKER1 to the end of the list
        start_index = card_list[0:joker_2_index]
        middle_index = card_list[joker_2_index:joker_1_index + 1]
        final_index = card_list[joker_1_index + 1:len(card_list)]
    else:
        start_index = card_list[0:joker_1_index]
        middle_index = card_list[joker_1_index:joker_2_index + 1]
        final_index = card_list[joker_2_index + 1:len(card_list)]
    # Create a new list with the splices.
    # Put the final slice first and the first slice last
    new_list = final_index + middle_index + start_index
    # Remove inputted list, add the newly created list to the inputted list
    card_list.clear()
    card_list += new_list


def insert_top_to_bottom(card_list):
    ''' (list of integers) -> NoneType
    This function takes the last number in the card_list, takes all number from
    0 to that index. It will then take that spliced value and move it from the
    top of the list to the bottom, just before the last value.
    REQ: card_list must be a list of integers, cannot be empty
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> insert_top_to_bottom(list1)
    >>> print(list1)
    [20, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15, 18, 21,
    24, 2, 5, 8, 11, 14, 17, 26]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 26, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 28]
    >>> insert_top_to_bottom(list2)
    >>> print(list2)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 26, 27, 9, 12, 15, 18, 21, 24,
    2, 5, 8, 11, 14, 17, 20, 28]
    >>> list3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 28, 26, 27, 9, 12, 15]
    >>> list3 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 6]
    >>> insert_top_to_bottom(list3)
    >>> print(list3)
    [19, 22, 25, 23, 3, 28, 26, 27, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17,
     20, 1, 4, 7, 10, 13, 16, 6]
    '''
    # Get the last integer in the card_list, set a variable to that value
    last_int = card_list[len(card_list) - 1]
    # Duplicate that variable incase the final number is 28
    true_int = last_int
    # If the final number is JOKER2, switch to JOKER1,
    # make the duplicate variable JOKER2
    if(last_int == JOKER2):
        last_int = JOKER1
        true_int = JOKER2
    # Cut a section of the first numbers out
    start_index = card_list[0: last_int]
    # Cut the second section of numbers, avoiding the last number
    final_index = card_list[last_int: len(card_list) - 1]
    # Create a new list from the previous splice, starting with the numbers
    # after the splice.
    new_list = final_index + start_index
    # Add in the last number of the original list
    new_list.append(true_int)
    # Clear the given list and add the new list to it
    card_list.clear()
    card_list += new_list


def get_card_at_top_index(card_list):
    ''' (list of integers) -> int
    This function looks at the first value in the card_list and returns the
    number at that index. If the first card is equal to JOKER2, then the value
    of JOKER1 is used.
    REQ: card_list must be a list of integers, cannot be empty
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_card_at_top_index(list1))
    4
    >>> list2 = [28, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 1, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_card_at_top_index(list2))
    26
    '''
    # Get the first card's value
    first_int = card_list[0]
    # If the first card is the joker2, set the first card to Joker1
    if(first_int == JOKER2):
        first_int = JOKER1
    # Get the value at the first card's index
    value = card_list[first_int]
    return value


def get_next_value(card_list):
    ''' (list of integers) -> int
    This function runs through all steps of the encryption algorithm and
    outputs a keystream value.
    REQ: card_list must be a list of integers, card_list cannot be empty
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_next_value(list1))
    25
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_next_value(list2))
    19
    '''
    # Call all the functions from the encryption algorithm
    move_joker_1(card_list)
    move_joker_2(card_list)
    triple_cut(card_list)
    insert_top_to_bottom(card_list)
    # Set the keysteam value to the final return statement and return
    key_stream_value = get_card_at_top_index(card_list)
    return key_stream_value


def get_next_keystream_value(card_list):
    """ (list of integers) -> int
    This function will run the encryption algorithm until a valid keystream is
    found (number from 1-26). Returns that new value.
    REQ: card_list must be a list of integers, card_list cannot be empty
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_next_keystream_value(list1))
    25
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(get_next_keystream_value(list2))
    19
    """
    # Create a variable, outside of the possible generated key values
    current_keystream_val = 0
    # Create a continuous loop, wait for a number to be within the requested
    # values
    while(not (current_keystream_val >= 1 and current_keystream_val <= 26)):
        current_keystream_val = get_next_value(card_list)
    return current_keystream_val


def process_message(card_list, message, function_type):
    """ (list of int, str, str) -> str
    Handler function for processing messages. Takes in a card_list, and message
    as well as the operation wished to be performed. Returns a complete message
    that is either encrypted or decrypted
    REQ: card_list must contain only ints, cannot be null
    REQ: message must be a string, cannot be empty
    REQ: function type must either be 'e'->encrypt or 'd'-> decrypt
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(process_message(list2, "HI", 'e'))
    'AC'
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list1 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(process_message(list2, "AC", 'd'))
    'HI'
    """
    # Clean the inputted message, removing numbers, spaces and \n
    message = clean_message(message)
    # Create an empty string for the new message
    new_message = ""
    # Loop through every letter in the message
    for letter in message:
        # Get a key value, encrypt or decrypt based on user input
        key_value = get_next_keystream_value(card_list)
        if (function_type == 'e'):
            new_letter = encrypt_letter(letter, key_value)
        else:
            new_letter = decrypt_letter(letter, key_value)
        # Add the new letter to the new string
        new_message += new_letter
    return new_message


def process_messages(card_list, message_list, function_type):
    """ (list of integers, list of strings, str) -> list of strings
    Function takes in a card_list, message_list and function_type then encodes
    or decodes the given messages based on the card_list. Function returns a
    list containing encrypted or decrypted messages.
    REQ: card_list cannot be empty, must contain 28 numbers
    REQ: message_list cannot be empty, messages must be strings
    REQ: function_type must be 'e' or 'd'
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(process_messages(list2, ["HI", "BOB"], 'e'))
    ['AC', 'JWI']
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 28, 23, 3, 6, 25, 27, 9, 12, 15]
    >>> list2 += [18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> print(process_messages(list2, ["AC", "JWI"], 'e'))
    ['HI', 'BOB']
    """
    encrypted_messages = []
    for message in message_list:
        new_message = process_message(card_list, message, function_type)
        encrypted_messages.append(new_message)
    return encrypted_messages


def read_messages(open_file_handler):
    """ (io.TextIOWrapper) -> list of str
    Function takes an open_file_handler and reads the lines, according to the
    formatting. Returns a list of all the lines, stripped of the newline char.
    REQ: open_file_handler must be in read mode
    """
    # Read the lines of the given file
    list_of_strings = open_file_handler.readlines()
    # Create an empty list to return to the main function
    new_list = list()
    # Loop through the strings from the file handler
    for message in list_of_strings:
        # Remove the \n character and add the new string to the return list
        new_message = message.replace("\n", "")
        new_list.append(new_message)
    return new_list


def read_deck(open_file_handler):
    """ (io.TextIOWrapper) -> list of ints
    Function takes an open_file_handler and reads the lines of the text file,
    parsing numbers out. Returns a list of integers taken from the file.
    REQ: open_file_handler must be in 'r' mode.
    REQ: open_file_handler must be a file that only contains numbers
    REQ: open_file_handler must split numbers by spaces
    """
    # Read the lines of the given file
    list_of_strings = open_file_handler.readlines()
    # Create an empty return list
    number_list = list()
    # Loop through the lines of the given file
    for line in list_of_strings:
        # Replace \n with empty space
        no_escape_line = line.replace("\n", "")
        # Split the line by spaces
        text_numbers = no_escape_line.split(" ")
        # Loop through every value in the line
        for numbers in text_numbers:
            # Make sure the line is not empty strings
            if(not (numbers == "")):
                # Cast the value to an int and add it to the list
                number_list.append(int(numbers))
    # Return the final list of values
    return number_list
