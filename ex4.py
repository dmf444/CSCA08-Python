
def insert(array1, array2, split_index):
    '''
    Insert takes array1 and splits it at the given split index, merges in
    array2 and re-adds any other pieces of array1.
    :param array1: list or str, cannot be null
    :param array2: list or str, cannot be null
    :param split_index: int, split_index >= 0 and split_index < len(arrray1)
    :return: list or string

    >>> insert("abc", "123", 3)
    'abc123'
    >>> insert([1,2,3,4,5], [42,44,42,44], 3)
    [1, 2, 3, 42, 44, 42, 44, 4, 5]
    '''
    # split the first array into first and second part
    begining_array = array1[0:split_index]
    end_array = array1[split_index: len(array1)]
    # Add first part to array2 and ending array
    return begining_array + array2 + end_array


def up_to_first(array1, object):
    '''
    Function that returns a list of everything in the list or string upto
    the first instance of object.
    :param array1: list or string, cannot be null
    :param object: any object, cannot be null
    :return: list or string
    >>> up_to_first("afl;dhflsdkfhslkdfhrifhgorlig", "s")
    'afl;dhfl'
    >>> up_to_first([1, 2, 8, 3, 4, 5, 6], 3))
    [1, 2, 8]
    '''
    if(object in array1):
        if(isinstance(array1, str)):
            end_list = ""
            flag = False
            for thing in array1:
                if(thing == object or flag):
                    flag = True
                else:
                    end_list += thing
        else:
            end_list = []
            flag = False
            for thing in array1:
                if(thing == object or flag):
                    flag = True
                else:
                    end_list.append(thing)
    else:
        end_list = array1
    return end_list


def cut_list(array1, index):
    '''
    Takes the given array, splits it at the given index and returns the
    array with the second half, then the first half
    :param array1: list, cannot be null
    :param index: int, cannot be null
    :return: list or string
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # Cut the array in halves
    first_cut = array1[0:index]
    second_cut = array1[index+1:len(array1)]
    # Return the array in the opposite order
    return second_cut + array1[index:index+1] + first_cut


def cut_list_challenge(array1, index):
    '''
    Takes the given array, splits it at the given index and returns the
    array with the second half, then the first half
    :param array1: list, cannot be null
    :param index: int, cannot be null
    :return: list or string
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # Return the array in the opposite order
    return array1[index+1:len(array1)] + array1[index:index+1] + \
        array1[0:index]
