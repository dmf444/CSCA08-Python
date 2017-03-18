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


def play2win(root: FormulaTree, turns: str, variables: str, values: str):
    if(len(turns) - len(values) == 1):
        check_var_0 = evaluate(root, variables, values + "0")
        check_var_1 = evaluate(root, variables, values + "1")
        if(check_var_0 == 1):
            next_move = 0
        else:
            next_move = 1
    else:
        current_player = turns[-(len(turns) - len(values))]
        if(current_player == "E"):
            next_move = 1
        else:
            next_move = 0
    return next_move


def draw_formula_tree(root: FormulaTree) -> str:
    r""" (FormulaTree) -> str
    This function takes in the root of a tree node, and builds the string to
    represent a printed tree node.
    REQ: root must not be None
    REQ: root must be a valid FormulaTree
    >>> a = draw_formula_tree(build_tree("(x+y)"))
    >>> print(a == "+\ty\n\tx")
    True
    >>> b = draw_formula_tree(build_tree("(-x+y)"))
    >>> print(b == "+\ty\n\t-\tx")
    True
    >>> c = draw_formula_tree(build_tree("(-x*y)"))
    >>> print(c == "*\ty\n\t-\tx")
    True
    >>> d = draw_formula_tree(build_tree("((-x+y)*z)"))
    >>> print(d == "*\tz\n\t+\ty\n\t\t-\tx")
    True
    """
    # Call the build_formula_helper function
    formula = draw_formula_tree_helper(root)
    # Remove the final \n added during the helper function
    formula = formula[:-1]
    # Return the built formula
    return formula


def draw_formula_tree_helper(root: FormulaTree, lvl=0, left=True) -> str:
    r""" (FormulaTree, int, bool) -> str
    This function takes in the root of a tree node, the current depth of the
    node and whether it is a right branch, and builds the string to
    represent a printed tree node.
    REQ: root must not be None
    REQ: root must be a valid FormulaTree
    REQ: left must only be true when the last node is "left" of the current
         node
    REQ: level must represent the current depth of the node from the root.
    >>> a = draw_formula_tree_helper(build_tree("(x+y)"))
    >>> print(a == "+\ty\n\tx\n")
    True
    >>> b = draw_formula_tree_helper(build_tree("(-x+y)"))
    >>> print(b == "+\ty\n\t-\tx\n")
    True
    >>> c = draw_formula_tree_helper(build_tree("(-x*y)"))
    >>> print(c == "*\ty\n\t-\tx\n")
    True
    >>> d = draw_formula_tree_helper(build_tree("((-x+y)*z)"))
    >>> print(d == "*\tz\n\t+\ty\n\t\t-\tx\n")
    True
    """
    # Create the return string as an empty string
    ret = ""
    # Create an empty left indent
    left_indent = ""
    # IF the branch has moved right
    if(not left):
        # Match the indent of the parent node + 1
        left_indent = "\t" * lvl
    # If this is a leaf node
    if(isinstance(root, Leaf)):
        # Check for indent, add the variable, and create a new line
        ret = left_indent + str(root.symbol) + "\n"
    # Otherwise, check if this is a notTreee node
    elif(isinstance(root, NotTree)):
        # Return the indent, the not symbol, a tab, and recurse throught the
        #  children of the not node. Consider them left nodes, for drawing
        ret = left_indent + str("-")+"\t" + draw_formula_tree_helper(
            root.children[0], lvl + 1)
    # Otherwise, we have some form of a binary tree
    else:
        # Add the indent and the symbol to the return string
        ret += left_indent + str(root.symbol) + "\t"
        # Check for left children (which should exist)
        if (root.children[1] is not None):
            # Recurse through the children in the node
            ret += draw_formula_tree_helper(root.children[1], lvl + 1)
        # check for right children (which should exist)
        if (root.children[0] is not None):
            # Recurse through the right children, setting the left boolean
            # to false
            ret += draw_formula_tree_helper(root.children[0], lvl + 1, False)
    # Return the fabricated string
    return ret


def boolean_compute(symbol: str, var_loc_1: str, var_loc_2: str):
    """ (str, str, str) -> str
    This function takes in a symbol, and two variables of either 0 or 1 and
    computes them as either not var1_loc_1 OR var_loc_1 and/or var_loc_2.
    This function returns the string representation of the outcome of the
    boolean formula, either '1' or '0'.
    REQ: symbol must be '*', '-' or '+'
    REQ: var_loc_1 must be '0' or '1'
    REQ: var_loc_2 must be '0' or '1' or ('-1' if symbol is '-')
    >>> boolean_compute("*", "0", "1")
    '0'
    >>> boolean_compute("*", "1", "1")
    '1'
    >>> boolean_compute("+", "0", "1")
    '1'
    >>> boolean_compute("+", "0", "0")
    '0'
    >>> boolean_compute("-", "0", "-1")
    '1'
    >>> boolean_compute("-", "1", "-1")
    '0'
    """
    # If the given symbol is an AND
    if(symbol == AND):
        # Check if either variable is false, which means AND fails
        if(var_loc_1 == '0' or var_loc_2 == '0'):
            # Return 0 (representing false)
            ret_num = "0"
        else:
            # Otherwise, and passed, return 1 - True
            ret_num = "1"
    # If our symbol is the OR symbol
    elif(symbol == OR):
        # Check if either one of the variables is true, meaning OR passes
        if(var_loc_1 == '1' or var_loc_2 == '1'):
            # Return true, because one was true
            ret_num = "1"
        else:
            # Otherwise both were false, return 0 as such
            ret_num = "0"
    # If the symbol is a NOT function
    elif(symbol == NOT):
        # Return the opposite string to the current one.
        if(var_loc_1 == "0"):
            # Return 1 if input was 0
            ret_num = "1"
        else:
            # Return 0 if input was 1
            ret_num = "0"
    return ret_num


def evaluate(root: FormulaTree, variables: str, values: str) -> int:
    """ (FormulaTree, str, str) -> int
    Function takes in a root, representing a root of a valid formula tree, a
    string of variables, representing the lower case letters in the formula
    and the string values, representing the values assigned to each letter.
    This function will compute the result of the formula with the given
    values assigned to the given variables. Returns either 0 or 1, if the
    formula computes to false, true; respectivly.
    REQ: len(variables) == len(values)
    REQ: values must be a string containing only '0' and '1'
    REQ: variables must contain all variables in the formula
    REQ: root != None
    REQ: root must be the root of a FormulaTree.
    >>> f = build_tree("(x*y)")
    >>> evaluate(f, "xy", "11")
    1
    >>> evaluate(f, "yx", "00")
    0
    >>> evaluate(f, "yx", "01")
    0
    >>> evaluate(build_tree("-(x*y)"), "xy", "11")
    0
    """
    # Call the helper, do all the work there, returns a string, not an int
    value = evaluate_helper(root, variables, values)
    # Cast to int, then return
    return int(value)


def evaluate_helper(root: FormulaTree, variables: str, values: str) -> str:
    """ (Formula Tree, str, str) -> str
    Function takes in a root, representing a root of a valid formula tree,
    a string of variables, representing the lowercase letters in the formula
    and the string values, representing the values assigned to each letter.
    The function will compute the result of the formula with the given
    values assigned to the given variables. Returns either, '0' or '1',
    if the formula computes to false/true.
    REQ: len(variables) == len(values)
    REQ: values must be a string containing only '0' and '1'
    REQ: variables must contain all variables in the formula
    REQ: root != None
    REQ: root must be the root of a FormulaTree.
    >>> f = build_tree("(x*y)")
    >>> evaluate_helper(f, "xy", "11")
    '1'
    >>> evaluate_helper(f, "yx", "00")
    '0'
    >>> evaluate_helper(f, "yx", "01")
    '0'
    >>> evaluate_helper(build_tree("-(x*y)"), "xy", "11")
    '0'
    """
    # If this is a binary tree node
    if(isinstance(root, AndTree) or isinstance(root, OrTree)):
        # Check if the left child is a leaf
        if(isinstance(root.children[0], Leaf)):
            # Save the variable and find the corresponding 1 or 0 in the
            # given list
            var1 = root.children[0]
            var1 = values[variables.find(var1.symbol)]
        # Otherwise, assume that there are more nodes to recurse through
        else:
            # Recurse through the rest of the children
            var1 = evaluate_helper(root.children[0], variables, values)
        # Check if the right child is a leaf node
        if(isinstance(root.children[1], Leaf)):
            # Save the variable and find the corresponding 1 or 0 in the
            # given list of values
            var2 = root.children[1]
            var2 = values[variables.find(var2.symbol)]
        # Else there are more nodes to check through
        else:
            # Recurse through the rest of the Tree's right node
            var2 = evaluate_helper(root.children[1], variables, values)
        # Given the left and right boolean values, compute the new boolean
        # value with the current +/* symbol
        number = boolean_compute(root.symbol, var1, var2)
    # Otherwise, this is a unary tree or a leaf tree
    else:
        # If the child is a leaf node
        if(isinstance(root.children[0], Leaf)):
            # Get the child variable
            not_var1 = root.children[0]
            # find the number corresponding to the given variable
            not_var1 = values[variables.find(not_var1.symbol)]
        else:
            # This is not a leaf node, recursivly call through the rest of
            # the node
            not_var1 = evaluate_helper(root.children[0], variables, values)
        # Evaluate the not answer, by calling boolean compute
        number = boolean_compute(root.symbol, not_var1, -1)
    # Return the final number
    return number


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
    """ (str) -> FormulaTree
    This function attempts to recursivly build a FormulaTree from a formula.
    Returns either the Tree, if the formula is valid, or None, if the
    formula has any errors. This function can also throw the IndexError if
    the function is invalid. Valid formulas follow the same rules as in
    build_tree.
    REQ: Formula must be all lower case letters
    REQ: len(formula) > 0
    REQ: formula exclusively contains lowercase letters, *, +, -, (, ) only
    RAISES: IndexError if the formula is invalid
    >>> a = build_tree("x+y")
    >>> print(a == None)
    True
    >>> b = build_tree("-(x)")
    >>> print(b == None)
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
    """
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
    print("NOT VALID FORMULAS")
    invalid_formulas = [
        '-(x)',
        '(-x)',
        '(x)',
        'x+y',
        '(-(x))',
        '-',
        'x+',
        '*x',
        'X',
        '((x))',
        '(x+y',
        'x+y)',
        'xx',
        '()',
        ')(',
        '(xy)',
        ')x+y(',
        '123',
        'abc',
        '-(-x)'
        ]
    for formula in invalid_formulas:
        t = build_tree(formula)
        print(t)
    print("VALID FORMULAS")
    valid_formulas = [
        'x',
        '-x',
        '(x+y)',
        '(x*y)',
        '(-x+y)',
        '(x+-y)',
        '(-x+-y)',
        '(-x*y)',
        '(x*-y)',
        '(-x*-y)',
        '-(x+y)',
        '-(x*y)',
        '((x+y)*z)',
        '-((x*y)+z)',
        '-((y*(-y*y))*-x)',
        '--x'
    ]
    for formula in valid_formulas:
        t = build_tree(formula)
        print(t)

    print(evaluate_helper(build_tree("--x"), "x", "1"))
    print(play2win(build_tree("-((y*(-y*y))*-x)"), "EA", "xy", "1"))
    print("ATTEMPT:")
    print(evaluate(build_tree("-((y*(-y*y))*-x)"), "yx", "01"))
    print(evaluate(build_tree("-((y*(-y*y))*-x)"), "yx", "00"))
    print(evaluate(build_tree("-((y*(-y*y))*-x)"), "yx", "11"))
    print(evaluate(build_tree("-((y*(-y*y))*-x)"), "yx", "10"))
    print("Draw That Tree!")
    t = draw_formula_tree(build_tree("((-a+b)*-(-c+d))"))
    print(t)
    print("MANUAL DRAWN:")
    print('*\t-\t+\td')
    print("\t\t\t-\tc")
    print("\t+\tb")
    print("\t\t-\ta")
    print("MANUAL DRAW 2:")
    print("*\t-\t+\tx\n\t\t\t-\ty\n\t+\ty\n\t\t-\tx")
    print("OTHER TREE:")
    print(draw_formula_tree(o))
    print("")
    print(draw_formula_tree(build_tree("(-y+x)")))