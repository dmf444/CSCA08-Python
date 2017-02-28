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
        count = 0
    else:
        count = in_list[0]
    return count

print(rmax([1, 2, 3]))
print(rmax([1, [2, 3]]))
print(rmax([[1], [2, [3]], [], [-4,5,6,7,8]]))