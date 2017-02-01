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


def get_node_at_index(head: 'SALBnode', number: 'int'):
    if(not (head == None)):
        curr = head
        for count in range(number):
            if(not(curr.next == None)):
                curr = curr.next
        if(curr.next == None):
            ret_node = None
        else:
            ret_node = curr
        return ret_node


salb3 = SALboard(6,  {2: 4, 5: 1})
salb2salbLL(salb3)
print(salb3)
