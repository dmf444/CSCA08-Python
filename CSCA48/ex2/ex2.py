from container import *
# from CSCA48.ex2.container import *


def banana_verify(source: 'str', goal_word: 'str', container, list_of_moves:
                  'list'):
    moded_word = source
    impossible = False
    new_word = ""
    while(len(list_of_moves) > 0 and not impossible):
        current_move = list_of_moves.pop(0)
        if(current_move == 'P'):
            # PUT
            try:
                first_letter = moded_word[0]
                container.put(first_letter)
                moded_word = moded_word[1:]
            except ContainerFullException:
                impossible = True
        elif (current_move == 'G'):
            # GET
            try:
                letter = container.get()
                new_word += letter
            except ContainerEmptyException:
                impossible = True
        else:
            # MOVE
            if(len(moded_word) > 0):
                letterz = moded_word[0]
                new_word += letterz
                if(len(moded_word) > 1):
                    moded_word = moded_word[1:]
    return (not impossible) and container.is_empty() and new_word == goal_word

# print(banana_verify("BANANA", "AAANNB", Container(), ["P", "M", "P", 'M',
#                                                      'P', 'M', 'G', 'G', 'G']
#                    ))
