
def radix_sort(numbers_in: list):
    # Copy the list in
    master_list = numbers_in[:]
    # Save the initial size of the list
    init_size = len(numbers_in)
    # Create a dictionary to store the values
    digits = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [],
              "7": [], "8": [], "9": []}
    curr_loc = -1
    # Continue until the master_list is empty
    while(len(master_list) != 0):
        # Sort through the master list
        for l in range(len(master_list)):
            # Get a number from the master list
            i = master_list[0]
            # Remove it from the master list
            master_list.remove(i)
            # Convert it to a string
            i = str(i)
            # Why bother with a try-except? I don't have to make 0's before
            # the numbers.
            try:
                # Backwards, get the index pertaining to the digit we're
                # considering
                numb = i[curr_loc]
                # Add the number to the correct dictionary list
                digits[str(numb)].append(int(i))
            # If the digit doesn't exist
            except IndexError:
                # Assume it's a zero
                digits["0"].append(int(i))
        # Check if the master list is empty AND if all the numbers are not in
        # the 0s column
        if(len(master_list) == 0 and len(digits["0"]) < init_size):
            # Move for current unit of measure back one digitplace
            curr_loc -= 1
            # Move all the numbers from their individual lists to the master
            for i in range(0, 10):
                # Add the digits
                master_list = master_list + digits[str(i)]
                # Empty the old list
                digits[str(i)].clear()
    return digits['0']
