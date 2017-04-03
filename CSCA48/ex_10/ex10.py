# from container import *


def banana_game(word1: str, word2: str, cont) -> bool:
    # Call helper Function, which does the work
    ret = banana_game_helper(word1, word2, cont)
    # Return the helper's answer
    return ret


def banana_game_helper(word1: str, word2: str, con, created_word="") -> bool:
    """
    Does all the work, too scared to put default params into Markus.
    """
    if(len(word1) == 0 and con.is_empty()):
        return word2 == created_word
    elif(len(word1) == 0 and not con.is_empty()):
        get_attempt = False
        if(not con.is_empty()):
            con_cop = con.copy()
            letter = con_cop.get()
            get_attempt = banana_game_helper(word1, word2, con_cop,
                                             created_word + letter)
        return get_attempt
    else:
        get_attempt = False
        move_attempt = False
        push_attempt = False
        if(not con.is_empty()):
            con_cop = con.copy()
            letter = con_cop.get()
            get_attempt = banana_game_helper(word1, word2, con_cop,
                                             created_word + letter)
        if(word1[0] == word2[len(created_word)]):
            move_attempt = banana_game_helper(word1[1:], word2, con.copy(),
                                              created_word + word1[0])
        try:
            con_copy = con.copy()
            con_copy.put(word1[0])
            push_attempt = banana_game_helper(word1[1:], word2, con_copy,
                                              created_word)
        except ContainerFullException:
            pass
        return get_attempt or move_attempt or push_attempt
