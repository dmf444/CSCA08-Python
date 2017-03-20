# This was the first half of the function "play2win", which got replaced
# by a permutation generator
"""
# If there is only one move left to make
    if(len(turns) - len(values) == 1):
        # Evaluate the game with both a zero and a one
        check_var_0 = evaluate(root, variables, values + "0")
        check_var_1 = evaluate(root, variables, values + "1")
        # If the current player is E
        if(current_player == "E"):
            # If 0 is a winning move and 1 is not
            if(check_var_0 == 1 and check_var_1 == 0):
                # Return 0
                next_move = 0
            # Else if 1 is a winning move and 0 is not
            elif(check_var_1 == 1 and check_var_0 == 0):
                # Return 1
                next_move = 1
            # Otherwise, return E's default move: 1
            else:
                next_move = 1
        # Otherwise the current player is A
        else:
            # If 0 is a winning move and 1 is not
            if(check_var_0 == 0 and check_var_1 == 1):
                # Return 0
                next_move = 0
            # Else if 1 is a winning move and 0 is not
            elif(check_var_1 == 0 and check_var_0 == 1):
                # Return 1
                next_move = 1
            # Otherwise, return A's default move: 0
            else:
                next_move = 0
    # Else there are several move to make still
    else:
"""