"""
# Copyright Nick Cheng, 2016; David Fernandes, 2017
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
    for node in range(size_of_board - 1, 0, -1):
        nodus = SALBnode(head)
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


def whowins(first: 'SALBnode', step1: 'int', step2: 'int') -> 'int':
    """ (SALBnode, int, int) -> int
    This function takes in a board representing a game of snakes and ladders, a
    player 1 step size and a player 2 step size then calculates which player
    will win the game. Function returns 1 if player one wins and 2 if player 2
    wins. If the stepsize for both players results with them getting into a
    loop, player two is automatically declared the winner.
    REQ: first is a pointer to the head of a circularly wrapped linked list.
    REQ: step1 is a non-negative number, step1 != None
    REQ: step2 is a non-negative number, step2 != None
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> whowins(board, 9, 10)
    2
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> whowins(board, 13, 12)
    2
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> whowins(board, 12, 3)
    1
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> whowins(board, 9, 3)
    2
    """
    # Check if either player will finish the board
    player_1 = willfinish(first, step1)
    player_2 = willfinish(first, step2)
    # If player 1 finishes, and player 2 does not
    if(player_1 and (not player_2)):
        # Set the winner to player 1
        winner = 1
    # If player 2 finishes and player 1 does not
    elif(player_2 and (not player_1)):
        # Set the winner to player 2
        winner = 2
    # If neither player finishes the board
    elif((not player_1) and (not player_2)):
        # Set player 2 as the winner
        winner = 2
    # If both players complete the board
    else:
        # Count the number of moves both players take
        player_1_count = player_step_count(first, step1)
        player_2_count = player_step_count(first, step2)
        # If player1 makes less moves
        if(player_1_count <= player_2_count):
            # Set player 1 as the winner
            winner = 1
        else:
            # otherwise, set player 2 as the winner
            winner = 2
    # Finally, return the winner
    return winner


def player_step_count(first: 'SALBnode', stepsize: 'int') -> 'int':
    """ (SALBnode, int) -> int
    This function takes a node representing a game of snakes and ladders, and a
    stepsize then calculates how many moves it will take the player to reach
    the end of the board. This function returns an int representation of how
    many moves the player made. If the player doesn't finish the board, this
    function will return the length of the board+1.
    REQ: first is a pointer to the head of a circularly linked list.
    REQ: stepsize is a non-negative int, stepsize != None
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> (player_step_count(board, 12))
    2
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> (player_step_count(board, 1))
    25
    """
    # NOTE: this function is a carbon copy of willfinish. This was done b/c
    # returning a tuple was counter the rules of this assignment.
    # Get the final node in the linked list
    finish_piece = get_tail_node(first)
    # Set the current node to the last element in the list
    current_node = finish_piece
    # Count the total number of nodes in the list
    board_size = count_nodes(first)
    # Create a counter for the while loop, also make a loop exit variable
    counter = 0
    landed_on_finish = False
    # Continue to loop through the board, so long as moves count is under board
    # count. (if not in a loop, player should visit every square only once)
    while(counter <= board_size and not landed_on_finish):
        # Move the player
        current_node = move_player(current_node, stepsize)
        # Check if this is the final node
        if(current_node == finish_piece):
            # IF this is, exit the loop
            landed_on_finish = True
        # This isn't, check if there is a snadder
        elif(current_node.snadder is not None):
            # Follow the snadder
            current_node = current_node.snadder
        # Increment the counter
        counter += 1
    # Return steps a player made
    return counter


def willfinish(first: 'SALBnode', stepsize: 'int') -> 'bool':
    """ (SALBnode, int) -> bool
    This function takes a node representing a game of snakes and ladders, and a
    stepsize then calculates whether the player will ever complete the board by
    hitting the last node in the linked list. Return True if the player does
    complete the board and False otherwise.
    REQ: first is a pointer to the head of a circularly linked list.
    REQ: stepsize is a non-negative int.
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> (willfinish(board, 9))
    False
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> (willfinish(board, 10))
    True
    >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
    >>> (willfinish(board, 25))
    False
    """
    # Get the final node in the linked list
    finish_piece = get_tail_node(first)
    # Set the current node to the last element in the list
    current_node = finish_piece
    # Count the total number of nodes in the list
    board_size = count_nodes(first)
    # Create a counter for the while loop, also make a loop exit variable
    counter = 0
    landed_on_finish = False
    # Continue to loop through the board, so long as moves count is under board
    # count. (if not in a loop, player should visit every square only once)
    while(counter <= board_size and not landed_on_finish):
        # Move the player
        current_node = move_player(current_node, stepsize)
        # Check if this is the final node
        if(current_node == finish_piece):
            # IF this is, exit the loop
            landed_on_finish = True
        # This isn't, check if there is a snadder
        elif(current_node.snadder is not None):
            # Follow the snadder, if found
            current_node = current_node.snadder
        # Increment loop counter
        counter += 1
    # Return if the player finished
    return landed_on_finish


def move_player(current_node: 'SALBnode', step: 'int') -> 'SALBnode':
    """ (SALBnode, int) -> SALBnode
    Given a node and a step size, this function move the pointer from
    current node to current_node + step size. Returns a pointer to the same
    linked list, but pointing at a different node.
    REQ: current_node is a pointer to the head of a circularly linked list.
    REQ: step is a non-negative number.
    """
    # Create a counter variable
    count = 0
    # Loop until the count is the step size
    while(count < step):
        # Move one node forward and increment the counter
        current_node = current_node.next
        count += 1
    # Return the list, with the pointer at the new head
    return current_node


def dualboard(head: 'SALBnode') -> 'SALBnode':
    """ (SALBnode) -> SALBNode
    Given a head reference to a SALBnode representing a board of snakes and
    ladders, this function will create a new board. The new board will have
    the same amount of nodes as the original, however, any snadders in the
    original board will point in reverse. I.E. if the original board has a
    snadder from 4 => 9, the new board will have a snadder from 9 => 4. This
    function will return the new linked list.
    REQ: head must be the start of a linked list, the final node in head
         must point back to head.

    """
    # Save a reference to the head node
    first = head
    # Create the first node of the linked list
    new_ll = SALBnode()
    # Create a var to represent the current location in the list
    work_var = new_ll
    # Get the size of the board, to loop through
    size_of_board = count_nodes(head)
    # Advance to second link
    head = head.next
    # Create default vars for the loop, loop exit and counter
    kill_loop = False
    count = 0
    # Loop until the size of the board is filled and loop exit is not true
    while (count < size_of_board and not kill_loop):
        # If this iteration is not the head node
        if(head != first):
            # Create and link a new node to the linked list
            work_var.next = SALBnode()
            work_var = work_var.next
            head = head.next
        else:
            # This is the head, link it back to the end
            work_var.next = new_ll
            kill_loop = True
    # Call helper function to create snadder references
    new_list = find_and_link_snadders(first, new_ll)
    # Return the completed list
    return new_list


def find_and_link_snadders(main_head: 'SALBnode', new_head: 'SALBnode'):
    """ (SALBnode, SALBnode) -> SALBnode
    This function takes two linked list, representing a game of snakes and
    ladders, of equivalent length, and maps snadders from one to the other.
    The snadders are placed in the second list in inverse order, I.E. if the
    first board has snadder from 4 => 9, thesecond board will have a snadder
    from 9 => 4. This function returns the second linked list, with snadders.
    REQ: main_head and new_head must be equivalent in length.
    REQ: main_head and new_head must be circular linked lists.
    REQ: main_head and new_head must be the head of a circular linked lists.
    """
    # Create variables to reference as the current position in the loop
    main_board = main_head
    backwards_board = new_head
    # Create a counter and get the size of the board
    count = 0
    board_size = count_nodes(main_head)
    # Loop through the entire board
    while(count < board_size):
        # If a snadder is found on the current SALBnode
        if(main_board.snadder is not None):
            # Start a second loop - find the companion node
            # Save found snadder location
            snadder_main = main_board.snadder
            # Save the second board's location as the pointer for the new
            # snadder.
            point_to_snadder = backwards_board
            # make new vars to increment the new loop
            backwards_board_2 = backwards_board.next
            main_board_2 = main_board.next
            # Coninue this loop until the snadder is found
            while(main_board_2 != snadder_main):
                # Increment the two lists if not yet found
                main_board_2 = main_board_2.next
                backwards_board_2 = backwards_board_2.next
            # Take the current second loop and point it to the saved pointer
            #  node
            backwards_board_2.snadder = point_to_snadder
        # Increment the board locations and the counter
        main_board = main_board.next
        backwards_board = backwards_board.next
        count += 1
    # return the head of the second list
    return new_head


def count_nodes(head):
    """ (SALBnode) -> int
     This function is used to count the number of nodes in a SALBnode. This
     function will return an integer representing the number of nodes.
     REQ: SALBnode != None, SALBnode must be circularly linked
     >>> board = salb2salbLL(SALboard(24, {3: 16, 21: 7}))
     >>> (count_nodes(board))
     24
     >>> board = salb2salbLL(SALboard(298, {3: 16, 21: 7}))
     >>> (count_nodes(board))
     298
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


def get_tail_node(head: 'SALBnode') -> 'SALBnode':
    """ (SALBnode) -> SALBnode
    This function takes in the head of a linked list, find the tail and
    returns it.
    REQ: head must be a linked list, with the tail referencing the head
    """
    # Set the current node and the last node
    curr = head.next
    last = head
    # Continue to loop through current until it's back at the head
    while(curr != head):
        # Move the current and last positions
        last = curr
        curr = curr.next
    # Return the end of the linked list - the last node
    return last
