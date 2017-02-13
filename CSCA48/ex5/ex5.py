def rsum(listr: 'list') -> 'int':
    if(len(listr) > 1):
        count = listr[0] + rsum(listr[1:])
    else:
        count = listr[0]
    return count


def rmax(listr: 'list') -> 'int':
    if(len(listr) == 1):
        max = listr[0]
    else:
        if(listr[0] > listr[1]):
            lisz = listr[0:1] + listr[2:]
            max = rmax(lisz)
        else:
            max = rmax(listr[1:])
    return max


def second_smallest_helper(listr: 'list') -> 'int':
    if(len(listr) > 2):
        smallest = (listr[0], listr[1])
    else:
        if(listr[0] > listr[1]):
            lisz = listr[0:1] + listr[2:]
            lisz.insert(0, listr[0])
            smallest = second_smallest_helper(lisz)
        else:
            smallest = second_smallest_helper(listr[1:])
    return smallest


def second_smallest(listr: 'list') -> 'int':
    (small1, small2) = second_smallest_helper(listr)
    return small2


def sum_max_min(listr):
    largest = rmax(listr)
    (smallest, s_s) = second_smallest_helper(listr)
    return largest + smallest

