"""
# Copyright Nick Cheng, 2016; David Fernandes 2017
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
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

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment

# Add your functions here.

AND = "*"
OR = "+"
NOT = "-"
LPARENTHESES = "("
RPARENTHESES = ")"


def build_tree(formula: str) -> FormulaTree:
    ''' (str) -> FormulaTree
    This function takes in a string, representing a boolean formula and
    returns the valid tree structure of that formula. If the function is
    invalid, the function will return None. Valid formula are as follows:
    1) All variables (single letters) must be lower case
    2) And/Or signs must have paretheses on either side of the variables
    3) Not signs must be directly applied to the variables
    4) Single variables cannot have parentheses
    REQ: len(formula) > 0
    REQ: formula exclusively contains lowercase letters, *, +, -, (, ) only
    >>> a = build_tree("x+y")
    >>> print(a == None)
    True
    >>> b = build_tree("-(x)")
    >>> print(b == None)
    True
    >>> c = build_tree("(x+Y)")
    >>> print(c == None)
    True
    >>> d = build_tree("(x+(y)*z)")
    >>> print(d == None)
    True
    >>> e = build_tree("(4+5)")
    >>> print(e == None)
    True
    >>> f = build_tree("(a+d)")
    >>> print(eval("OrTree(Leaf('a'), Leaf('d'))") == f)
    True
    '''
    # First, check if all variables are lowercase within the function
    if(formula.islower()):
        try:
            # Attempt to use recursion to make the tree
            tree = tree_builder(formula)
        # Extraneous parentheses and mismatched parentheses will crash the
        # build function with an IndexError. Catch that error and return None,
        # because formula is invalid.
        except IndexError:
            tree = None
    # The variables contained an upper case - the formula is invalid
    else:
        tree = None
    return tree


def tree_builder(formula: str) -> FormulaTree:
    # Check if the formula starts with a not symbol
    if(formula[0] == NOT):
        # Recursively call the tree again.
        child_tree = tree_builder(formula[1:])
        # This line will get changed, unless the child_tree returns None
        formula_tree = child_tree
        # Check if the child tree is not None (all sub trees were valid)
        if(child_tree is not None):
            # Add the sub tree to a not root, then return
            formula_tree = NotTree(child_tree)
    # Check if the formula starts with a brace, signifying a +/* upcoming
    elif(formula.startswith("(")):
        # Strip off the braces from the formula (we assume it's valid)
        stripped_brackets = formula[1:-1]
        # Create a variable to count the number of braces, midpoint and
        # if the midpoint has been found
        mid_point = 0
        brace_count = 0
        is_found = False
        # NOTE: How this works - Assume valid. Braces must open and close.
        # Count all openings, and all closing. When that count is 0,
        # we've found our midpoint, representing * or +.
        # Loop until midpoint is found
        while(not is_found):
            # Should we find a Left Parentheses, add 1 to the counter
            if(stripped_brackets[mid_point] == LPARENTHESES):
                brace_count += 1
            # If we find a Right parentheses, remove 1 from the counter
            elif(stripped_brackets[mid_point] == RPARENTHESES):
                brace_count -= 1
            # If we hit 0 on the brace count and we've found an */+
            if(brace_count == 0 and (stripped_brackets[mid_point] == AND or
                                     stripped_brackets[mid_point] == OR)):
                # Exit the loop
                is_found = True
            else:
                # Otherwise, increase the midpoint index, keep searching
                mid_point += 1
        # Assuming the midpoint was found, everything after it's the right tree
        # everything before it is the left tree
        # Recursively call the build function with that parameter.
        left_tree = tree_builder(stripped_brackets[:mid_point])
        right_tree = tree_builder(stripped_brackets[mid_point + 1:])
        # Default the return to None, incase one of the child nodes is None
        formula_tree = None
        # Check if the child nodes are None
        if(left_tree is not None and right_tree is not None):
            # If they're not, figure out what the midpoint symbol was
            # If it's the AND
            if(stripped_brackets[mid_point] == AND):
                # Create an AND tree
                formula_tree = AndTree(left_tree, right_tree)
            else:
                # Otherwise, create an OR tree
                formula_tree = OrTree(left_tree, right_tree)
    # Not an bracket nor a Not, either leaf or invalid
    else:
        # If this is a leaf, the length should be 1
        if(len(formula) > 1):
            # Found a length greater than 1, formula has an error
            formula_tree = None
        else:
            # Return a FormulaTree with the leaf of the variable
            formula_tree = Leaf(formula)
    return formula_tree


if(__name__ == "__main__"):
    t = build_tree("((((x+y)+y)+y)*((r*(r+u))*s))")
    print(t)
    t = build_tree("-((f+(-e*f))*-(e*-c))")
    print(t)
    t = build_tree("(((x+y)*(y+z))*(-y+-z))")
    print(t)
    o = build_tree("(a+(b+(c+(d+(e+(f+(g+(h+(i+(j+(k+(l+(m+(n+(o+(p+(q+(r+(s+(t+(u+(v+(w+(x+(y+z)))))))))))))))))))))))))")
    l = eval("OrTree(Leaf('a'), OrTree(Leaf('b'), OrTree(Leaf('c'), OrTree(Leaf('d'), OrTree(Leaf('e'), OrTree(Leaf('f'), OrTree(Leaf('g'), OrTree(Leaf('h'), OrTree(Leaf('i'), OrTree(Leaf('j'), OrTree(Leaf('k'), OrTree(Leaf('l'), OrTree(Leaf('m'), OrTree(Leaf('n'), OrTree(Leaf('o'), OrTree(Leaf('p'), OrTree(Leaf('q'), OrTree(Leaf('r'), OrTree(Leaf('s'), OrTree(Leaf('t'), OrTree(Leaf('u'), OrTree(Leaf('v'), OrTree(Leaf('w'), OrTree(Leaf('x'), OrTree(Leaf('y'), Leaf('z'))))))))))))))))))))))))))")
    print(o == l)
    t = build_tree("(a+d)")
    print(t)

    import doctest
    doctest.testmod()