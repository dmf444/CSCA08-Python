# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                      'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                      'X': 23, 'Y': 24, 'Z': 25}


def clean_message(message):
    '''(str) -> str
    This function takes in a String message and cuts out all spaces, then puts
    everything in uppercase. Returns the new string
    REQ: message != null, message can only contain alphabetic charaters
    >>> clean_message("no body knows the trouble ive seen")
    'NOBODYKNOWSTHETROUBLEIVESEEN'
    >>> clean_message("FHSLR D")
    'FHSLRD'
    '''
    # Replace all spaces in the message with empty strings
    new_message = message.replace(" ", "")
    # Convert the entire message to uppercase, then return
    new_message = new_message.upper()
    return new_message


def encrypt_letter(letter, key_value):
    '''(str, int) -> str
    This function takes in a letter, converts it to a number and applies the key_value to that number, then returns a
    letter, corresponding to the newly generated number.
    REQ: key_value >= 0 and <= 25
    REQ: letter != '' and letter has one Character
    >>> encrypt_letter('A', 3)
    'D'
    >>> encrypt_letter('Z', 6)
    'F'
    >>> encrypt_letter('W', 30)
    'A'
    '''
    # Get the numerical value of the given letter
    letter_key = letters_to_numbers[letter]
    # Add the letter number to the given key value
    crypt_key = letter_key + key_value
    # Modulus the new number against 26 (or length of dict)
    new_key = crypt_key % len(letters_to_numbers)
    # Inverse the dictionary, therefore giving numbers from letters
    result = {}
    for next_key in letters_to_numbers:
        next_value = letters_to_numbers[next_key]
        result[next_value] = next_key
    # Get the new letter and return it
    new_letter = result[new_key]
    return new_letter


def decrypt_letter(letter, key_value):
    '''(str, int) -> str
    This function takes in a letter, converts it to a number and removes the key_value from that number, then returns a
    letter, corresponding to the original text of the encrypted message.
    REQ: key_value >= 0 and <= 25
    REQ: letter != '' and letter has one Character
    >>> decrypt_letter('A', 45)
    'H'
    >>> decrypt_letter('Z', 504)
    'P'
    >>> decrypt_letter('H', 5)
    'C'
    '''
    # Get the numerical value of the given letter
    letter_key = letters_to_numbers[letter]
    # Add the letter number to the given key value
    crypt_key = letter_key - key_value
    # Modulus the new number against 26 (or length of dict)
    new_key = crypt_key % len(letters_to_numbers)
    # Inverse the dictionary of letters to numbers, therefore giving numbers from letters
    result = {}
    for next_key in letters_to_numbers:
        next_value = letters_to_numbers[next_key]
        result[next_value] = next_key
    # Get the new letter and return it
    new_letter = result[new_key]
    return new_letter


def swap_cards(card_list, index):
    ''' (list, int) -> NoneType
    This function takes a card_list, finds a specific card at an index and swaps in with the card next to it. This
    function treats the card_list as circular, if index is the highest number in the list, the card will be swapped
    with the lowest int.
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
    '''
    # If the index is an edge case (is the last card)
    if(index == len(card_list) - 1):
        # Make a temporary variable to store the first number, set the last number to the first number, and vice-versa
        temp_value = card_list[0]
        card_list[0] = card_list[index]
        card_list[index] = temp_value
    else:
        # Get the value above the index, save it to a temp variable. Set index + 1's value to index and index's value to
        # the temp variable
        temp_value = card_list[index + 1]
        card_list[index + 1] = card_list[index]
        card_list[index] = temp_value


def move_joker_1(card_list):
    '''
    This function takes in a card_list, finds the joker value (27) and moves it up 1 position.
    (list of integers) -> NoneType
    REQ: card_list must be a list of integers
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_1(list1)
    >>> print(list1)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 27, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 27]
    >>> move_joker_1(list2)
    >>> print(list2)
    [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1]
    >>> list3 = [27, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1]
    >>> move_joker_1(list3)
    >>> print(list3)
    [4, 27, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 23, 26, 1]
    '''
    # Create a flag for exiting the while loop and an index for where the joker is
    joker_found = False
    current_index = 0
    # As long as the joker is not found, continue the loop
    while(not joker_found):
        # Get the card at the current index, if it's the joker, set the flag to true, otherwise, add 1 to index
        card = card_list[current_index]
        if(card == JOKER1):
            joker_found = True
        else:
            current_index += 1
    # once the joker has been found, swap it with the card above it
    swap_cards(card_list, current_index)


def move_joker_2(card_list):
    '''
    This function takes in a card_list, finds the second joker value (28) and moves it up the list 2 positions. This
    function treats the dec as circular and will move Joker2 back to the begining of the list if it cannot move to a
    higher index.
    (list of integers) -> NoneType
    REQ: card_list must be a list of integers
    >>> list1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> move_joker_2(list1)
    >>> print(list1)
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 28, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 28, 26]
    >>> move_joker_2(list2)
    >>> print(list2)
    [28, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26, 1]
    >>> list3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26, 28]
    >>> move_joker_2(list3)
    >>> print(list3)
    [4, 28, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26, 1]
    '''
    # Create a flag for exiting the while loop and an index for where the joker is
    joker_found = False
    current_index = 0
    while(not joker_found):
        # Get the card at the current index, if it's the joker, set the flag to true, otherwise, add 1 to index
        card = card_list[current_index]
        if(card == JOKER2):
            joker_found = True
        else:
            current_index += 1
    # once the joker has been found, swap it with the card above it, then again with the card above it
    swap_cards(card_list, current_index)
    swap_cards(card_list, (current_index + 1) % len(card_list))


def triple_cut(card_list):
    ''' (list of integer) -> NoneType
    This function takes a card_list, finds all number above the second joker and put them at the bottom of the list.
    At the same time it takes all number below the first joker and puts them at the top of the list. If the jokers are
    on the top or bottom of the list, no numbers are changed.
    REQ: card_list must be a list of integers, cannot be empty
    REQ: card_list.index(JOKER1) > card_list.index(JOKER2)
    >>> list3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> triple_cut(list3)
    >>> print(list3)
    [2, 5, 8, 11, 14, 17, 20, 26, 28, 9, 12, 15, 18, 21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6]
    >>> list2 = [28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 27]
    >>> triple_cut(list2)
    >>> print(list2)
    [28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 27]
    >>> list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6, 28, 27, 9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26]
    >>> triple_cut(list2)
    >>> print(list2)
    [9, 12, 15, 18, 21, 24, 2, 5, 8, 11, 14, 17, 20, 26, 28, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 23, 3, 6]
    '''
    # Get the index of the two jokers
    joker_1_index = card_list.index(JOKER1)  # card value of 27
    joker_2_index = card_list.index(JOKER2)  # card value of 28
    # Cut the card list into three parts, representing all cards from 0 to JOKER2, JOKER2 to JOKER1 and JOKER1 to the
    # end of the list
    start_index = card_list[0:joker_2_index]
    middle_index = card_list[joker_2_index:joker_1_index + 1]
    final_index = card_list[joker_1_index + 1:len(card_list)]
    # Create a new list with the splices. Put the final slice first and the first slice last
    new_list = final_index + middle_index + start_index
    # Remove all traces of the inputted list, add the newly created list to the inputted list
    card_list.clear()
    card_list += new_list

import doctest
doctest.testmod()