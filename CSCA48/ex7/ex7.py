def edit_distance(s1: str, s2: str) -> int:
    """
    Function takes in a string representing the first word, and another
    string, representing the second word. The function will count all changes
    needed to make s1 -> s2.
    REQ: len(s1) == len(s2)
    >>> edit_distance("dog", "cog")
    1
    >>> edit_distance("chatty", "cathri")
    4
    """
    # Just count differences in the letter placement
    # Once no more letters, we've hit 0.
    if(len(s1) == 0):
        count = 0
    else:
        # If the letters are the same - no need to add to count
        if(s1[0] == s2[0]):
            count = 0 + edit_distance(s1[1:], s2[1:])
        else:
            # Otherwise, add to the count
            count = 1 + edit_distance(s1[1:], s2[1:])
    return count


def perms(s: str) -> set:
    # Read docs in Helper for info
    sets = perms_helper(s, "")
    return sets


def perms_helper(s: str, old_s: str, iteration=0) -> set:
    """
    Function takes in a string, old string and an iteration count and attempts
    to find every combo of every word. Returns a set containing all the
    possible combinations of the letters.
    """
    if(len(s) < 2):
        count = set(s)
    # Check if we've narrowed it down to two letters
    elif(len(s) == 2):
        # Create the set, add in the original letters, plus both combos
        # of the last two letters
        count = set()
        count.add(old_s + s)
        count.add((old_s + s[1] + s[0]))
    else:
        # Recall the function, making the original word smaller and the
        # old_string bigger
        count = perms_helper(s[1:], old_s + s[0])
        # Add in all the other combinations of the letters by recalling the
        # function. Check to see if we've iterated over them before. (and
        # stop an infinite loop).
        if(iteration < len(s + old_s)):
            # Some union magic.... it seems to work, also add one to iteration
            count.update(perms_helper(s[1:] + s[0], old_s, iteration + 1))
    return count


def subsequence_helper(s1: str, s2: str, word="", count=0) -> bool:
    """
    Function takes in two strings, s1 and s2 and effectivly tests if s1 in s2.
    Returns true if the first string can be parsed out from s2 and false
    otherwise.
    """
    if(len(s2) == 0):
        is_sub = False
    elif(s1 == word):
        is_sub = True
    else:
        if(s1[count] != s2[0]):
            is_sub = subsequence_helper(s1, s2[1:], word, count)
        else:
            word += s2[0]
            is_sub = subsequence_helper(s1, s2, word, count + 1)
    return is_sub


def subsequence(s1: str, s2: str) -> bool:
    """
    See docstring for subsequence_helper
    """
    return subsequence_helper(s1, s2)
