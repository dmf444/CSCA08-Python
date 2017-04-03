from ex10 import *
import time
import random
import gc

from CSCA48.ex4.Queue import Queue
from CSCA48.ex4.Stack import Stack
from CSCA48.ex_10.Bucket import Bucket

SHOW_LOG = bool(input("Show details? (Blank for No):"))


def recursive_bench(string):
    # just randomness
    if len(string) == 1:
        result = string
    elif len(string) % 2 == 0:
        result = string[-1] + string[len(string)-1::-1]
    else:
        result = string[0] + string[:0:-1]
    return result


def random_string(length=100):
    # more randomness
    string = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabce' +
                                   'dfghijklmnopqrstuvwxyz1234567890')
                     for i in range(length))
    return string


def swap_adjacent(string):
    # makes a string that surely can be bucketed
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            if i+1 < len(string):
                result = result + string[i+1]
            else:
                result = result + string[-1]
        else:
            result = result + string[i-1]
    return result


def run(factor=100, loop=True):
    iterations = 10
    while iterations > 0:
        gc.disable()
        base = []
        score = []
        result = []
        for i in range(iterations):
            start = time.time()
            strings = [random_string(10*factor) for i in range(50)]
            [recursive_bench(string) for string in strings]
            base_line = time.time() - start
            base.append(base_line)
            strings = [random_string() for i in range(factor)]
            start = time.time()
            result.append(all([banana_game(strings[i], strings[i][::-1],
                          Stack()) for i in range(factor)]))
            result.append(all([banana_game(strings[i],
                                           strings[i][-1]+strings[i][:-1],
                                           Queue())
                               for i in range(factor)]))
            result.append(all([banana_game('asdasjdlkasjd',
                                           swap_adjacent('asdasjdlkasjd'),
                                           Bucket())
                               for i in range(factor)]))
            instance = time.time() - start
            score.append(instance)
            if SHOW_LOG:
                print ('Time', '{}/{}:\t'.format(str(i+1), iterations),
                       (instance))
        result = all(result)
        average = sum(score)/float(len(score))
        base_line = sum(base)/float(len(base))
        if SHOW_LOG:
            print("system's speed:\t\t{}".format(base_line), 'seconds')
            print ("average run Time:\t{}".format(average), 'seconds')
        final_score = 10*(base_line/average)
        print("data size:\t\t{}".format(factor) + '\n' +
              "efficiency rating:\t{0:.2f}".format(final_score))
        if not result:
            print("ERROR")
        gc.enable()
        if loop:
            factor = input("Custom data size:")
            try:
                factor = int(factor)
            except:
                factor = 0
        else:
            iterations = -1
    return final_score


if __name__ == '__main__':
    while True:
        efficiency = [run(10*i, False) for i in range(1, 11)]
        final_efficiency = sum(efficiency)/float(len(efficiency))
        print("Average efficiency rating: {0:.2f}".format(final_efficiency))
        input("Enter to retry")