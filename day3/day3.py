def get_num(line):
    nums = []
    line = line[:-1]
    special_characters = "!@#$%^&*()-+?_=,<>/"

    for special_char in special_characters:
        line = line.replace(special_char,'.')
    for char in line.split('.'):
        if char.isnumeric() == True and char not in nums:
            nums.append(int(char))

    return nums

def check_special_char_first_line(num, num_idx, line, below_line):

    special_characters = "!@#$%^&*()-+?_=,<>/"
    num_len = len(num)
    line_len = len(line)


    if num_idx > 0 and num_idx < line_len - 1:
        if any(c in special_characters for c in line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
            
        if any(c in special_characters for c in below_line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
    
    if num_idx == 0 and num_idx < line_len - 1:

        if any(c in special_characters for c in line[num_idx : num_idx + num_len + 1]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx : num_idx + num_len + 1]):
            return int(num)

    if num_idx > 0 and num_idx == line_len - 1:

        if any(c in special_characters for c in line[num_idx -1 : num_idx + num_len]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx -1 : num_idx + num_len]):
            return int(num)

def check_special_char_middle_line(num, num_idx, line, above_line, below_line):

    special_characters = "!@#$%^&*()-+?_=,<>/"
    num_len = len(num)
    line_len = len(line)


    if num_idx > 0 and num_idx + num_len < line_len - 1:
        if any(c in special_characters for c in line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
            
        if any(c in special_characters for c in below_line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
    
    if num_idx == 0:

        if any(c in special_characters for c in line[num_idx : num_idx + num_len + 1]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx : num_idx + num_len + 1]):
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx : num_idx + num_len + 1]):
            return int(num)

    if num_idx + num_len == line_len - 1 :

        if any(c in special_characters for c in line[num_idx -1 : ]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx -1 : ]):
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx -1 : ]):
            return int(num)


def check_special_char_last_line(num, num_idx, line, above_line):

    special_characters = "!@#$%^&*()-+?_=,<>/"
    num_len = len(num)
    line_len = len(line)
    
    if num_idx == 0:

        if any(c in special_characters for c in line[num_idx : num_idx + num_len + 1]):
            return int(num)

        if any(c in special_characters for c in above_line[num_idx : num_idx + num_len + 1]):
            return int(num)

    if num_idx + num_len == line_len -1:

        if any(c in special_characters for c in line[num_idx -1 : num_idx + num_len]):
            return int(num)

        if any(c in special_characters for c in above_line[num_idx -1 : num_idx + num_len]):
            return int(num)
    
    if num_idx > 0 and num_idx + num_len < line_len -1:

        if any(c in special_characters for c in line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)
            
        if any(c in special_characters for c in above_line[num_idx - 1 : num_idx + num_len + 1]):
            return int(num)

    return 'Not correct'

def read_file(filename):
    with open("day3.txt") as f:
        lines = f.readlines()
    return lines

def part_1():

    lines = read_file("day3.txt")
    sum_all = 0

    for line_idx in range(len(lines)):

        corrected_nums = []

        line = lines[line_idx]

        nums = get_num(line)
        
        if line_idx == 0:

            below_line = lines[line_idx + 1]
            
            
            for num in sorted(nums,reverse=True):
                num = str(num)
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]

                s = '.'*len(num)
                line = line.replace(num,s)

                for num_idx in num_idxs:
                    correct_num = check_special_char_first_line(num, num_idx, line, below_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)



        if line_idx == len(lines) - 1:

            above_line = lines[line_idx - 1]

            for num in sorted(nums, reverse=True):
                num = str(num)
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]

                s = '.'*len(num)
                line = line.replace(num,s)

                for num_idx in num_idxs:
                    correct_num = check_special_char_last_line(num, num_idx, line, above_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)


        if line_idx > 0 and line_idx < len(lines) - 1:

            above_line = lines[line_idx - 1]
            below_line = lines[line_idx + 1]

            for num in sorted(nums, reverse=True):
                num = str(num)
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]
                s = '.'*len(num)
                line = line.replace(num,s)
                
                for num_idx in num_idxs:
                    correct_num = check_special_char_middle_line(num, num_idx, line, above_line, below_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)

        # print(line_idx, corrected_nums)
        sum_all = sum_all + sum(corrected_nums)
    print("Part 1: ", sum_all)

def part_2():
    
    lines = read_file("day3.txt")





    print("Part 2: ")
    return "Part 2: "


def main():

    part_1()

    part_2()


if __name__ == "__main__":
    main()