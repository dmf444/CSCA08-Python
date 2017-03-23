
def radix_sort(numbers_in: list):
    master_list = numbers_in[:]
    init_size = len(numbers_in)
    digits = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [],
              "7": [], "8": [], "9": []}
    curr_loc = -1
    while(len(master_list) != 0 or len(digits['1']) != 0 or
          len(digits['2']) != 0 or len(digits['3']) != 0 or
          len(digits['4']) != 0 or len(digits['5']) != 0 or
          len(digits['6']) != 0 or len(digits['7']) != 0 or
          len(digits['8']) != 0 or len(digits['9']) != 0):
        for l in range(len(master_list)):
            i = master_list[0]
            master_list.remove(i)
            i = str(i)
            try:
                numb = i[curr_loc]
                digits[str(numb)].append(int(i))
            except IndexError:
                digits["0"].append(int(i))
        if(len(master_list) == 0 and len(digits["0"]) < init_size):
            curr_loc -= 1
            for i in range(0, 10):
                master_list = master_list + digits[str(i)]
                digits[str(i)].clear()
    return digits['0']

print(radix_sort([1,39, 18, 20, 4565, 999]))