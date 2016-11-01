

def percent_to_gpv(mark):
    '''
    percent_to_gpv is a function that returns the Grade Point Value, in float
    for any given percentage mark.
    :param mark: int, 0 < mark < 100
    :return: float
    >>> percent_to_gpv(85)
    4.0
    >>> percent_to_gpv(81)
    3.7
    >>> percent_to_gpv(77)
    3.3
    >>> percent_to_gpv(73)
    3.0
    '''

    # Switch through all mark values in the given table, making sure to watch
    # for edge cases and setting the correct gpa
    if(mark >= 85):
        gpv = 4.0
    elif(mark >= 80):
        gpv = 3.7
    elif(mark >= 77):
        gpv = 3.3
    elif(mark >= 73):
        gpv = 3.0
    elif(mark >= 70):
        gpv = 2.7
    elif(mark >= 67):
        gpv = 2.3
    elif(mark >= 63):
        gpv = 2.0
    elif(mark >= 60):
        gpv = 1.7
    elif(mark >= 57):
        gpv = 1.3
    elif(mark >= 53):
        gpv = 1.0
    elif(mark >= 50):
        gpv = 0.7
    else:
        gpv = 0.0
    return gpv


def card_namer(card_value, card_suit):
    '''
    Given a card_value and a card_suit, this function will return a valid
    card from the deck
    :param card_value: String; accepted values are 1-9, T, A, J, Q, K
    :param card_suit: String; accepted values are H, C, S, D
    :return: String
    >>> card_namer("3", "S")
    '3 of Spades'
    >>> card_namer("T", "D")
    '10 of Diamonds'
    >>> card_namer("K", "T")
    'CHEATER!'
    '''
    # Create card values based on human readablility
    if(card_value == 'A'):
        true_value = 'Ace'
    elif(card_value == 'T'):
        true_value = '10'
    elif(card_value == 'J'):
        true_value = 'Jack'
    elif(card_value == 'Q'):
        true_value = 'Queen'
    elif(card_value == 'K'):
        true_value = 'King'
    else:
        true_value = card_value

    # Create card suit based on human readablility
    if(card_suit == 'D'):
        true_name = "Diamonds"
    elif(card_suit == 'S'):
        true_name = "Spades"
    elif(card_suit == 'C'):
        true_name = "Clubs"
    elif(card_suit == 'H'):
        true_name = "Hearts"
    else:
        return "CHEATER!"

    return true_value + " of " + true_name


def my_str(object):
    '''
    Converts any given object into a string. If given a string, it will echo
    it back; given a boolean: return 'YES' or 'NO'; given an integer: return
    'Small Number' if object <= 10, 'Medium Number' if 11 < object < 99 and
    'Big Number' if object >= 100; given a float: round to two decimal places
    and return 'I dunno" for all other types.
    :param object: Object
    :return: String
    >>> isinstance("Hello",str)
    True
    >>> isinstance(True,bool)
    True
    >>> my_str("Hello")
    Hello
    >>> my_str(False)
    NO
    >>> my_str(42)
    Medium Number
    >>> my_str(42.0)
    42.0
    >>> my_str(3.1415926)
    3.14
    >>> my_str([1, 2, 3])
    I dunno
    '''
    if(type(object) == str):
        output = object
    elif(type(object) == bool):
        if(object):
            output = "YES"
        else:
            output = "NO"
    elif(type(object) == int):
        if(object <= 10):
            output = "Small Number"
        elif(object <= 99):
            output = "Medium Number"
        else:
            output = "Large Number"
    elif(type(object) == float):
        # output = "%.2f" % object <--Better code, just doesn't satify given ex
        output = str(round(object, 2))
    else:
        output = "I dunno"
    return output
