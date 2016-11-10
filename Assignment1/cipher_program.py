"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck2.txt'
MSG_FILENAME = 'secret6.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # TODO: Third letter is broken, must fix
    deck_file_handle = open(DECK_FILENAME, "r")
    card_int_list = cipher_functions.read_deck(deck_file_handle)
    deck_file_handle.close()
    message_file_handle = open(MSG_FILENAME, "r")
    message_list = cipher_functions.read_messages(message_file_handle)
    message_file_handle.close()
    encryption_list = cipher_functions.process_messages(card_int_list, message_list, MODE)
    encrypted_msg = ""
    for encrypted_message in encryption_list:
        encrypted_msg += encrypted_message
    print(encrypted_msg)

main()
