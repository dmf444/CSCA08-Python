"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.


def salb2salbLL(salb: 'dict') -> SALBnode:
    """ (dict) -> SALBnode
    This function takes in a salb dictionary representation of snakes and
    ladders board and returns an identical board with the same snadder
    locations in the form of a linked list.
    REQ: salb must be a dictionary representation of a snakes and ladders board
    """
    # Get data from dict board
    size_of_board = salb.numSquares
    snadder_dict = salb.snadders
    # Get all values that have or are linked
    important_nums = list(snadder_dict.values()) + list(snadder_dict.keys())
    # Empty dict that holds a reference from board to node (eg. 1=> SalbNode())
    node_link_dict = {}
    # Create the last node in the linked list
    head = SALBnode()
    # Save the last node to loop the list
    last_node = head
    # IMPORTANT EDGE CASE - the last node is in a snadder
    if(size_of_board in important_nums):
        node_link_dict[size_of_board] = head
    # Build the nodes, backwards, from size -1 to 0
    for node in range(size_of_board-1, 0, -1):
        nodus = SALBnode(head)
        ###############################################
        ##################################
        ############################
        # ### I MUST BE DELETED!!!!
        nodus.number = node
        # Check if the number is part of a snadder, if so, add it to dict
        if(node in important_nums):
            node_link_dict[node] = nodus
        # Reset head to new node
        head = nodus
    #################
    # Make snadders
    #################
    # Loop through dict version's keys
    for key in snadder_dict.keys():
        # Get the acompanying values
        value = snadder_dict[key]
        # Pull nodes from dictionary required for key/value match
        from_snadder = node_link_dict[key]
        to_snadder = node_link_dict[value]
        # Make sure something didn't error and become none
        if(not(to_snadder == None and from_snadder == None)):
            # Map the snadder as required
            from_snadder.snadder = to_snadder
    # Finally loop the last node to the first
    last_node.next = head
    return head


def willfinish(first, stepsize):
    # operates on principal of passing the head.
    # if player passes head, he is not in loop
    # otherwise, he has to be in a loop

def dualboard(head):
    first = head
    new_ll = SALBnode()
    work_var = new_ll
    size_of_board = count_nodes(head)
    if((head is not None) and (head.next is not None)):
        head = head.next
    kill_loop = False
    count = 0
    while (count < size_of_board and not kill_loop):
        if(head != first):
            work_var.next = SALBnode()
            work_var = work_var.next
            head = head.next
        else:
            work_var.next = new_ll
            kill_loop = True
    new_list = find_and_link_snadders(first, new_ll)
    return new_list


def find_and_link_snadders(main_head, new_head):
    ######################################################
    # Stack and Track
    # Method:
    # Loop through all places in given head START FROM HEAD
    # On finding a snadder -> make new vars, sync to head and continue
    # around loop until finding node, make copy, return to main loop
    main_board = main_head
    backwards_board = new_head
    count = 0
    board_size = count_nodes(main_head)
    while(count < board_size):
        if(main_board.snadder is not None):
            snadder_main = main_board.snadder
            point_to_snadder = backwards_board
            backwards_board_2 = backwards_board.next
            main_board_2 = main_board.next
            while(main_board_2 != snadder_main):
                main_board_2 = main_board_2.next
                backwards_board_2 = backwards_board_2.next
            backwards_board_2.snadder = point_to_snadder
        main_board = main_board.next
        backwards_board = backwards_board.next
        count += 1
    return new_head


def count_nodes(head):
    """ (SALBnode) -> int
     This function is used to count the number of nodes in a SALBnode. This
     function will return an integer representing the number of nodes.
     REQ: SALBnode != None, SALBnode must be circularly linked
    """
    # Start with an empty count
    count = 0
    # Create a current reference and loop exit variable
    curr = head
    exit_loop = False
    # Loop through the list until exit loop is called
    while(curr.next is not None and not exit_loop):
        # Add one to counter, set current to next in list
        count += 1
        curr = curr.next
        # Check if should exit loop, b/c back at head
        if(curr == head):
            exit_loop = True
    # Return the accrued count
    return count


salb3 = SALboard(6,  {2: 4, 1: 5})
e = salb2salbLL(salb3)
f = dualboard(e)
g = count_nodes(e)
print(g)






def testing(__salb1__, size):
    # first node is the output of the salb2salbLL function
    __head__ = __salb1__
    # get the max width by rounding down the square root of numSquares
    __maxwidth__ = math.floor(math.sqrt(size))

    try:
        # copy the nodes into a list
        __squares__ = []
        # set node to be the head of the list
        __node__ = __head__
        # for every node
        for o in range(0, size):
            # append it to the list
            __squares__.append(__node__)
            # move one forward
            if __node__.next is not None:
                __node__ = __node__.next
            else:
                print("Null pointer at node.next\n One of your links is not",
                      "pointing to the right place :O")
        # empty start:end dict
        __snadders__ = {}
        # run through the list and copy the start:end pairs from the nodes
        for p in range(0, len(__squares__)):
            if __squares__[p].snadder is not None:
                __snadders__[p + 1] = __squares__.index(
                    __squares__[p].snadder) + 1
        # keep records of the start and end of each snadder from the dict
        __start__ = list(__snadders__.keys())
        # __start__.sort()
        __end__ = list(__snadders__.values())
        # __end__.sort()

    except (IndexError, TypeError) as ex:
        print(
            "Oh no! Something broke, double check your code!")
    else:
        if list(__snadders__.keys()) != __start__:
            print("Your linked list snadders and your dictionary snadders",
                  "don't match 0_0\n")

    # counter to reference the current square's number
    __counter__ = 1
    try:
        # for each row in the board
        for k in range(0, int(math.ceil(size / __maxwidth__))):
            # make a string to add the squares into
            row = ""
            # for each column in the board
            for j in range(int(k * __maxwidth__), int((k + 1) * __maxwidth__)):
                # if the square has a snadder
                if __counter__ in __start__:
                    # print a square with the number of the index in it
                    row += ("[_" + str(__start__.index(__counter__)) + "S_]")
                elif __counter__ in __end__:
                    # print a square with the number of the index in it
                    row += ("[_" + str(__end__.index(__counter__)) + "E_]")
                elif __counter__ <= size:
                    # print an empty square
                    row += ("[____]")
                # add one to the counter
                __counter__ += 1
                # move to the next node
                __node__ = __node__.next
            # print the row
            print(row, "\n\n")
    except IndexError:
        print("Graph failed :(\nDouble check your code!")


if __name__ == "__main__":
    import math
    import doctest

    print("NORMAL BOARD")
    board = salb2salbLL(SALboard(16, {1: 2, 6: 4, 5: 14}))
    testing(board, 16)
    print("\n")
    print("DUAL BOARD")
    testing(dualboard(board), 16)
