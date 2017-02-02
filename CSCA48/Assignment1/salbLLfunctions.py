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


def dualboard(head):
    first = head
    new_ll = SALBnode()
    work_var = new_ll
    if((head is not None) and (head.next is not None)):
        head = head.next
    kill_loop = False
    while ((head is not None) and (head.next is not None) and not kill_loop):
        if(head != first):
            work_var.next = SALBnode()
            work_var = work_var.next
            head = head.next
        else:
            work_var.next = new_ll
            kill_loop = True
    new_list = stack_and_track(first, new_ll)
    return new_list


def stack_and_track(first, new_ll):
    ######################################################
    # Stack and Track
    # Method:
    # Loop through all places in given head START FROM HEAD
    # On finding a snadder -> make new vars, sync to head and continue
    # around loop until finding node, make copy, return to main loop
    main_ll = first.next
    first1 = first
    new_ll1 = new_ll
    backward_ll = new_ll.next
    # Catch for first iteration only
    # TODO
    loop_escape = False
    while(main_ll is not None and backward_ll is not None and not loop_escape):
        if(first1 != main_ll):
            if(main_ll.snadder is not None):
                snadder_main = main_ll.snadder
                point_to_snadder = backward_ll
                backward_ll1 = backward_ll.next
                main_ll1 = main_ll.next
                while(main_ll1 != snadder_main):
                    main_ll1 = main_ll1.next
                    backward_ll1 = backward_ll1.next
                backward_ll1.snadder = point_to_snadder
            main_ll = main_ll.next
            backward_ll = backward_ll.next
        else:
            loop_escape = True
    return new_ll


salb3 = SALboard(6,  {2: 4, 1: 5})
e = salb2salbLL(salb3)
f = dualboard(e)
print(f)
