from formula_game_functions import *
from random import randint

NOT, AND, OR = '-', '*', '+'
OPS = {0: NOT, 1: AND, 2: OR}
VARS = {0: 'x', 1: 'y', 2: 'z'}


# CREDIT: Anonymous
def generate_formula(layers, var='x'):
    """(int[, str]) -> str

    Builds and returns a random formula of with a given number of layers,
    such that a formula with a layer of zero is simply the variable itself.

    NOTE: formulas with layers > 6 will get VERY LARGE!

    REQ: layers >= 0
    REQ: var == var.lower() and len(var) == 1
    """
    if layers == 0:
        formula = var
    else:
        operator = OPS[randint(0, 2)]
        if operator == NOT:
            formula = generate_formula(layers - 1, var)
            if formula[0] != NOT:
                formula = NOT + formula
        else:
            sub_formula = generate_formula(layers - 1, var)
            other_var = VARS[randint(0, 2)]
            other_formula = generate_formula(randint(0, layers), other_var)
            formula = '(' + other_formula + operator + sub_formula + ')'
    return formula

# CREDIT : So Tsz Cheuk
if __name__ == '__main__':
    import time
    slowest_time = 0
    total_time = time.time()
    for i in range(0,58):
        formula = generate_formula(i)
        start = time.time()
        root = build_tree(formula)
        end = time.time()
        time_used = end-start
        slowest_time = max(slowest_time, time_used)
    total_time = time.time() - total_time
    print('Total Time used: ' + str(total_time) + ' seconds \n' +
          'Slowest execution time: ' + str(slowest_time) + ' seconds')
