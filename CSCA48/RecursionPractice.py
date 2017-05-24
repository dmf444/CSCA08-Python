def same_string(s1, s2):
    """
    Returns true iff s1 is same as s2
    :param s1: string
    :param s2: string
    REQ: len(s1) == len(s2)
    :return: bool, true iff s1 == s2.
    """
    if(len(s1) > 0):
        if(s1[0] == s2[0]):
            is_same = same_string(s1[1:], s2[1:])
        else:
            is_same = False
    else:
        is_same = True
    return is_same

print(same_string("Pizza", "Pizza"))

def almost_same_string(s1, s2):
    """
    Return True iff s1 and s2 have at most 1 different char
    REQ: len(s1) == len(s2)
    """
    if(s1 == "" and s2 == ""):
        res = True
    elif(s1[0] != s2[0]):
        res = same_string(s1[1:], s2[1:])
    else:
        res = almost_same_string(s1[1:], s2[1:])
    return res
print(almost_same_string("Pizza", "pizza"))


def almost_same_string_1(s1, s2) -> int:
    if(s1 == "" and s2 == ""):
        count = 0
    elif(s1[0] != s2[0]):
        count = 1 + almost_same_string_1(s1[1:], s2[1:])
    else:
        count = 0 + almost_same_string_1(s1[1:], s2[1:])
    return count

print(almost_same_string_1("PizzaIsGood", "pizzaisgood"))
