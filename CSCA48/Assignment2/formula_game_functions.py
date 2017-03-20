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
    """ (FormulaTree, str, str, str) -> int
    This function takes in the root of a FormulaTree, the turn order of E/A as
    a string, the variables in the formula as a string and the values of the
    variables then returns the best move for the current player to make. If
    choosing 0 is a winning move and 1 isn't, function will return 0. If
    choosing 1 is a winning move and 0 isn't, function will return 1. For all
    other cases, function will return the default values for A and E being
    0 and 1, respectively.
    REQ: len(turns) > len(values)
    REQ: root must be a valid formula tree
    REQ: variables must contain all lowercase variables in the root
    REQ: values must only contain '1's and '0's
    REQ: turns must only contain 'E's and 'A's
    >>> a = build_tree("x")
    >>> b = build_tree("-y")
    >>> print(play2win(a, 'E', 'x', ''))
    1
    >>> print(play2win(b, 'E', 'y', ''))
    0
    >>> c = build_tree('((x+y)+(y+x))')
    >>> print(play2win(c, 'EE', 'xy', '0'))
    1
    >>> d = build_tree("(((w+x)*(w+x))+((y+z)*(y+z)))")
    >>> print(play2win(d, 'AEAE', 'wxyz', ''))
    0
    """
    # Get the current player
    current_player = turns[-(len(turns) - len(values))]
    # Generate all possible permutations of valid combinations
    possible_permutations = permutation_generator(len(variables), values)
    # Cast the possible permutations to a list
    pos_perms_list = list(possible_permutations)
    # Create a list to store moves that will win the game
    winning_moves = []
    # Loop through the permutation list
    for value in pos_perms_list:
        # Evaluate the possible combination
        result = evaluate(root, variables, value)
        # If the player is we are checking for is E and the result was 1
        if(current_player == "E" and result == 1):
            # This is a winning strategy, let's save it
            # Also, strip the default, given values for the save
            winning_moves.append(value[len(values):])
        # Otherwise, if the current player is a and the evaluation was 0
        elif(current_player == "A" and result == 0):
            # This is a winning strategy for A, save it
            # Also, strip the default, given values for the save
            winning_moves.append(value[len(values):])
    # If there is no default strategy for the player
    if(len(winning_moves) == 0):
        # Return default player's number
        if(current_player == "E"):
            # E's default is 1
            next_move = 1
        else:
            # A's default is 0
            next_move = 0
    # Otherwise, there are some amount of valid moves the player can make
    else:
        # Create two boolean variable to check if there are both 0's and 1's
        # in the winning combination list
        zero_found = False
        one_found = False
        # Loop through all valid winning moves
        for win in winning_moves:
            # If the winning move starts with "0"
            if(win[0] == "0"):
                # Switch the boolean, there is a zero
                zero_found = True
            # If the winning move starts with a "1"
            elif(win[0] == "1"):
                # Switch the boolean, there is a one
                one_found = True
        # If there is a 0 and a 1 in the winning set
        if(zero_found and one_found):
            # No clear win path, return player's default move
            if(current_player == "E"):
                # 1 for player E
                next_move = 1
            else:
                # 0 for player A
                next_move = 0
        # If there are only zeros in the winning moves set
        elif(zero_found):
            # Zero is part of a winning strategy, return that
            next_move = 0
        # Otherwise, only ones were found
        else:
            # One is part of a winning strategy, return that
            next_move = 1
    return next_move


def permutation_generator(max_size: int, values: str) -> set:
    """ (int, str) -> set
    Function take in a max_size of string to generate, a string of values and
    returns a set of all possible combinations of 1s and 0s up to the maximum
    size.
    REQ: max_size > len(values)
    REQ: values must be a string of 1s and 0s
    >>> print(permutation_generator(2, "") == {"00", "01", "10", "11"})
    True
    >>> print(permutation_generator(1, "") == {"0", "1"})
    True
    >>> print(permutation_generator(2, "0") == {"01", "00"})
    True
    >>> t = {"0100", "0101", "0110", "0111"}
    >>> print(permutation_generator(4, "01") == t)
    True
    """
    # Check if the values just needs one more number
    if(len(values) + 1 == max_size):
        # If it does, create a set
        ret_set = set()
        # Add the current values plus a 0 to the new set
        ret_set.add(values + "0")
        # Add the current values plus a 1 to the new set
        ret_set.add(values + "1")
    # Otherwise, there needs to be more permutations
    else:
        # Recurse through the generator, with 0 appended to the value list
        first = permutation_generator(max_size, values + "0")
        # Recurse through the generator with a 1 appended to the value list
        second = permutation_generator(max_size, values + "1")
        # Make the first set the union of the first and second set
        first.update(second)
        # Return the first set
        ret_set = first
    # Return the set
    return ret_set


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
        ret = left_indent + str("-") + "\t" + draw_formula_tree_helper(
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
    elif(isinstance(root, Leaf)):
        number = values[variables.find(root.symbol)]
    # Otherwise, this is a unary tree
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

    a = 'x'
    b = '-y'
    c = '(x+y)'
    d = '(-x*y)'
    e = '((x+y)+(y+x))'
    f = '(((x+y)*(x+y))+((a+b)*(a+b)))'

    aa = build_tree(a)
    bb = build_tree(b)
    cc = build_tree(c)
    dd = build_tree(d)
    ee = build_tree(e)
    ff = build_tree(f)

    A1 = play2win(aa, 'E', 'x', '')
    A2 = play2win(aa, 'A', 'x', '')
    A3 = play2win(bb, 'E', 'y', '')
    A4 = play2win(bb, 'A', 'y', '')
    # 1001
    A5 = play2win(cc, 'AA', 'xy', '')
    A6 = play2win(cc, 'EE', 'xy', '')
    A7 = play2win(cc, 'AE', 'xy', '0')
    A8 = play2win(cc, 'EA', 'xy', '0')
    A9 = play2win(cc, 'AE', 'xy', '1')
    A10 = play2win(cc, 'EA', 'xy', '1')
    A11 = play2win(dd, 'AA', 'xy', '')
    A12 = play2win(dd, 'EE', 'xy', '')
    A13 = play2win(dd, 'AE', 'xy', '0')
    A14 = play2win(dd, 'EA', 'xy', '0')
    A15 = play2win(dd, 'AE', 'xy', '1')
    A16 = play2win(dd, 'EA', 'xy', '1')
    A17 = play2win(ee, 'AA', 'xy', '')
    A18 = play2win(ee, 'AA', 'xy', '1')
    A19 = play2win(ee, 'EE', 'xy', '')
    A20 = play2win(ee, 'EE', 'xy', '0')
    A21 = play2win(ee, 'AE', 'xy', '')
    A22 = play2win(ee, 'AE', 'xy', '0')
    A23 = play2win(ee, 'EA', 'xy', '')
    A24 = play2win(ee, 'EA', 'xy', '1')
    # 0110100010100011011
    A25 = play2win(ff, 'EEEE', 'xyab', '101')
    A26 = play2win(ff, 'EEEE', 'xyab', '10')
    A27 = play2win(ff, 'EEEE', 'xyab', '1')
    A28 = play2win(ff, 'EEEE', 'xyab', '')
    A29 = play2win(ff, 'AAAA', 'xyab', '101')
    A30 = play2win(ff, 'AAAA', 'xyab', '10')
    # A31 = play2win(ff, 'AAAA', 'xyab', '1')
    A32 = play2win(ff, 'AAAA', 'xyab', '')
    A33 = play2win(ff, 'AEAE', 'xyab', '101')
    A34 = play2win(ff, 'AEAE', 'xyab', '10')
    A35 = play2win(ff, 'AEAE', 'xyab', '1')
    A36 = play2win(ff, 'AEAE', 'xyab', '')
    # 011110001010
    B = str(A1)+str(A2)+str(A3)+str(A4)+str(A5)+str(A6)+str(A7)+str(A8)+str(A9)+str(A10)+str(A11)+str(A12)+str(A13)+str(A14)+str(A15)+str(A16)+str(A17)+str(A18)+str(A19)+str(A20)+str(A21)+str(A22)+str(A23)+str(A24)+str(A25)+str(A26)+str(A27)+str(A28)+str(A29)+str(A30)+str(A32)+str(A33)+str(A34)+str(A35)+str(A36)
    print(B)
    print("10010110100010100011011011110001010")
    if(B == '10010110100010100011011011110001010'):
        print("WIINNING")
    else:
        print("Damn Fool!")
