"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck2.txt'
MSG_FILENAME = 'totrans1.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # Open the deck file, in read mode
    deck_file_handle = open(DECK_FILENAME, "r")
    # Read the card list into a variable
    card_int_list = cipher_functions.read_deck(deck_file_handle)
    # CLOSE THE DECK FILE
    deck_file_handle.close()
    # Open the message file
    message_file_handle = open(MSG_FILENAME, "r")
    # Read the messages into a variable
    message_list = cipher_functions.read_messages(message_file_handle)
    # CLOSE THE MESSAGE FILE!!
    message_file_handle.close()
    # Encrypt/decrypt the message
    encryption_list = cipher_functions.process_messages(card_int_list,
                                                        message_list, MODE)
    # Empty string variable to parse the message
    encrypted_msg = ""
    # For every word in the encryption list
    for encrypted_message in encryption_list:
        # Turn the list into one word
        encrypted_msg += encrypted_message
    # Print out the message
    print(encrypted_msg)

main()
