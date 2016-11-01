# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    '''
    this function takes in a String message and cuts out all spaces, then puts
    everything in uppercase. Returns the new string
    (str) -> str
    REQ: message != null, message can only contain alphabetic charaters
    >>> clean_message("no body knows the trouble ive seen")
    'NOBODYKNOWSTHETROUBLEIVESEEN'
    >>> clean_message("FHSLR D")
    'FHSLRD'
    '''
    new_message = message.replace(" ", "")
    new_message = new_message.upper()
    return new_message

