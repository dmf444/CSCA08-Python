# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                      'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                      'X': 23, 'Y': 24, 'Z': 25}


def clean_message(message):
    '''
    This function takes in a String message and cuts out all spaces, then puts
    everything in uppercase. Returns the new string
    (str) -> str
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
    '''
    This function takes in a letter, converts it to a number and applies the key_value to that number, then returns a
    letter, corresponding to the newly generated number.
    (str, int) -> str
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
    '''
    This function takes in a letter, converts it to a number and removes the key_value from that number, then returns a
    letter, corresponding to the original text of the encrypted message.
    (str, int) -> str
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
    # Inverse the dictionary, therefore giving numbers from letters
    result = {}
    for next_key in letters_to_numbers:
        next_value = letters_to_numbers[next_key]
        result[next_value] = next_key
    # Get the new letter and return it
    new_letter = result[new_key]
    return new_letter

import doctest
doctest.testmod()