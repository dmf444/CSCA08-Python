# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: [REDACTED]
# MarkUs Login: [REDACTED]
#

PUZZLE1 = '''
tlkutqyu
hyrreiht
inokdcne
eaccaayu
riainpaf
rrpnairb
ybybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyyrreihtpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences(TEST_PUZZLE, 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # Take original puzzle, find occurences then rotate it 3 times and do the same
    left_to_right = lr_occurrences(puzzle, word)
    top_to_bottom = lr_occurrences(rotate_puzzle(puzzle), word)
    right_to_left = lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word)
    bottom_to_top = lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), word)
    # Return the sum of all the occurences
    return left_to_right + top_to_bottom + right_to_left + bottom_to_top

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> boolean
    Returns whether a word can be found horizontally forwards or reversed
    inside a given puzzle. Returns True if the word is found on the horizontal, false otherwise.
    REQ: puzzle != ""; word != ""

    >>> in_puzzle_horizontal("xaxy \n yaaa", 'xa')
    True
    >>> in_puzzle_horizontal("xaxy \n yaaa", 'xn')
    False
    '''
    # Using lr_occurences, if there is > 0 instances, we set a value to true
    # Check Backwards and Forwards
    left_to_right = lr_occurrences(puzzle, word) > 0
    right_to_left = lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word) > 0
    return left_to_right or right_to_left

# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> boolean
    Returns whether a word can be found vertically forwards or reversed
    inside a given puzzle. Returns True if the word is found on the vertical, false otherwise.
    REQ: puzzle != ""; word != ""

    >>> in_puzzle_vertical("xaxy \n yaaa", 'aaa')
    False
    >>> in_puzzle_vertical("xaxs \n yaaa", 'sa')
    True
    '''
    # Check if there is an occurrence by testing if the lr_occurences returns greater than 0.
    top_to_bottom = lr_occurrences(rotate_puzzle(puzzle), word) > 0
    bottom_to_top = lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), word) > 0
    # not exclusive, so return if either variable has True
    return top_to_bottom or bottom_to_top

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> boolean
    Returns whether a word can be found inside a given puzzle.
    Returns True if the word is found, false otherwise.
    REQ: puzzle != ""; word != ""

    >>> in_puzzle("xaxy \n yaaa", 'aaa')
    True
    >>> in_puzzle("xaxy \n yaaa", 'B.Harrington_is_the_best_prof_ever')
    False
    '''

    # Using the two previous functions, check if the word exists horizontally or vertically
    in_horizontal = in_puzzle_horizontal(puzzle, word)
    in_vertical = in_puzzle_vertical(puzzle, word)
    # Return True if either or is True
    return in_horizontal or in_vertical

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    ''' (str, str) -> boolean
    Returns whether the given word is exclusively horizontal or vertical.
    Returns true if exclusivly horizontal, true if exclusivly vertical, false otherwise.
    REQ: puzzle != ""; word != ""

    >>> in_exactly_one_dimension("xaxy \n yaaa", 'aaa')
    True
    >>> in_exactly_one_dimension("xaxy \n yaaa", 'xa')
    False
    '''
    # Check if the word is in the vertical and also check if in the vertical
    in_horizontal = in_puzzle_horizontal(puzzle, word)
    in_vertical = in_puzzle_vertical(puzzle, word)

    # Return if the word is exclusivly in the horizontal or in the vertical
    return (in_horizontal and (not in_vertical)) or (in_vertical and (not in_horizontal))

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    ''' (str, str) -> boolean
    Returns whether a given word is in the puzzle and all instances are horizontal.
    If all word instances are horizontal, return True. If the word is not in the puzzle, return True.
    Otherwise return False.
    REQ: puzzle != ""; word != ""

    >>> all_horizontal("xaxy \n yaaa", 'aaa')
    True
    >>> all_horizontal("xaxy \n yaaa", 'xy')
    False
    >>> all_horizontal("xaxy \n yaaa", 'Star_Trek_Wars')
    True
    '''

    # Must check if there are occurrences of l->r and r->l or nothing at all
    left_to_right = lr_occurrences(puzzle, word) >= 0
    right_to_left = lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word) >= 0
    # Check if there is any vertical instances of 'word'
    is_in_vertical = in_puzzle_vertical(puzzle, word)
    # Return if there is an l-> or r->l and make sure there are no vertical words
    return (left_to_right or right_to_left) and (not is_in_vertical)

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    ''' (str, str) -> boolean
    Returns if there is at most 1 instance of word vertically in the puzzle.
    If there is one an instance vertically, return true. If there are no instances, return true
    If there is more than 1 instance, return false
    REQ: puzzle != ""; word != ""

    >>> all_horizontal("xaxy \n yaaa", 'xy')
    True
    >>> all_horizontal("xaxy \n yyyy", 'xy')
    False
    >>> all_horizontal("xaxy \n yaaa", 'IgotAGoodMarkFromHarrington')
    True
    '''
    # Check if the word occurs once or less in top-to-bottom and bottom-to-top
    top_to_bottom = lr_occurrences(rotate_puzzle(puzzle), word) <= 1
    bottom_to_top = lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), word) <= 1
    # Return true if the first or second are true and both are not true
    return (top_to_bottom or bottom_to_top) and not(bottom_to_top and top_to_bottom)



def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name))

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(rotate_puzzle(puzzle), name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), name))

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))
    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')

# *task* 7: call do_tasks on PUZZLE2  and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, "nick")
# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, "nick"))
# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'thierry'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE2, 'thierry'))
