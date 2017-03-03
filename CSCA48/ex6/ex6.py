def rsum(in_list: list) -> int:
    '''
    This function takes in a list containing other lists and integers,
    and returns an integer, being the sum of all ints in the list.
    :param in_list: [list, int]
    :return: int, sum of all ints in list
    '''
    # Check for base case
    if(len(in_list) > 0):
        # check if this is a list, if so, recall fn on list
        if(isinstance(in_list[0], list)):
            count = rsum(in_list[0]) + rsum(in_list[1:])
        else:
            # Not a list, parse rest of function, add current num
            count = in_list[0] + rsum(in_list[1:])
    else:
        # Base case, nothing in list
        count = 0
    return count


def rmax(in_list: list) -> int:
    """
    Goes throught a list. Finds max number in the list.
    :param in_list: list of ints and lists
    :return: largest int in main list
    """
    if(len(in_list) > 1):
        first = in_list[0]
        if(isinstance(first, list)):
            first = rmax(first)
        second = in_list[1]
        if(isinstance(second, list)):
            second = rmax(second)
        if(second > first):
            count = rmax([second] + in_list[2:])
        else:
            count = rmax([first] + in_list[2:])
    elif (len(in_list) == 0):
        count = float("-inf")
    else:
        count = in_list[0]
    return count


def sum_max_min(inlist: list)-> int:
    """
    This function finds the sum of the largest and smallest numbers in a list.
    Function returns the sum of the numbers in the list
    """
    # Call helper fuction, find largest and smallest
    (smallest, biggest) = max_min_helper(inlist)
    # Add the two together
    added = smallest + biggest
    # Return
    return added


def max_min_helper(inlist: list) -> (int, int):
    """
    This function takes in a list and computes the max and minimum numbers
    of the list, then returns a tuple containing those numbers.
    :param inlist: list containing numbers and lists
    :return: Tuple containing the largest and smallest number
    """
    if(len(inlist) == 1):
        if(isinstance(inlist[0], list)):
            count = max_min_helper(inlist[0])
        else:
            count = (inlist[0], inlist[0])
    elif(len(inlist) >= 2):
        var = len(inlist)//2
        one = max_min_helper(inlist[:var])
        two = max_min_helper(inlist[var:])
        if(two[1] > one[1]):
            one = (one[0], two[1])
        if(two[0] < one[0]):
            one = (two[0], one[1])
        count = one
    else:
        count = (float("inf"), float("-inf"))
    return count


def second_smallest(in_list: list) -> int:
    """
    This function takes in a list and finds the second smallest
    value inside the list. This function operates with nested lists.
    REQ: nested list may only contain lists and ints
    RETURNS: second_smallest number in the list
    """
    (smallest, second_smaller) = second_smallest_helper(in_list)
    if(second_smaller == float("inf") or second_smaller == float("-inf")):
        second_smaller = smallest
    return second_smaller


def second_smallest_helper(inlist: list) -> (int, int):
    """
    Returns the two smallest numbers in the list. Uses recursion over the
    .sort method
    :param inlist: nested list, containing only ints and lists
    :return: tuple of the two smallest ints
    """
    if (len(inlist) == 1):
        if (isinstance(inlist[0], list)):
            count = second_smallest_helper(inlist[0])
        else:
            count = (inlist[0], inlist[0])
    elif (len(inlist) >= 2):
        half_pt = len(inlist) // 2
        first_cut = second_smallest_helper(inlist[:half_pt])
        second_cut = second_smallest_helper(inlist[half_pt:])
        if (first_cut[0] < second_cut[0]):
            first_cut = (first_cut[0], second_cut[0])
        elif (first_cut[0] > second_cut[0]):
            first_cut = (second_cut[0], first_cut[0])
        count = first_cut
    else:
        count = (float("inf"), float("-inf"))
    return count
