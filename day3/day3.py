def get_num(line):
    nums = []
    special_characters = "!@#$%^&*()-+?_=,<>/"

    for special_char in special_characters:
        line = line.replace(special_char,'.')
    
    for char in line.split('.'):
        if char.isnumeric() == True and char not in nums:
            nums.append(char)
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



    if num_idx > 0 and num_idx < line_len - 1:
        if any(c in special_characters for c in line[num_idx - 1 : num_idx + num_len + 1]):
            # print(num, line[num_idx - 1 : num_idx + num_len + 1])
            return int(num)
            
        if any(c in special_characters for c in below_line[num_idx - 1 : num_idx + num_len + 1]):
            # print(num, below_line[num_idx - 1 : num_idx + num_len + 1])
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx - 1 : num_idx + num_len + 1]):
            # print(num, above_line[num_idx - 1 : num_idx + num_len + 1])
            return int(num)
    
    if num_idx == 0 and num_idx < line_len - 1:

        if any(c in special_characters for c in line[num_idx : num_idx + num_len + 1]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx : num_idx + num_len + 1]):
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx : num_idx + num_len + 1]):
            return int(num)

    if num_idx > 0 and num_idx == line_len - 1:

        if any(c in special_characters for c in line[num_idx -1 : num_idx + num_len]):
            return int(num)

        if any(c in special_characters for c in below_line[num_idx -1 : num_idx + num_len]):
            return int(num)
        
        if any(c in special_characters for c in above_line[num_idx -1 : num_idx + num_len]):
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

    if num_idx == line_len -1:

        if any(c in special_characters for c in line[num_idx -1 : num_idx + num_len]):
            return int(num)

        if any(c in special_characters for c in above_line[num_idx -1 : num_idx + num_len]):
            return int(num)
    
    if num_idx > 0 and num_idx < line_len -1:
        # print('btw', num, 'idx :', num_idx)
        if any(c in special_characters for c in line[num_idx - 1 : num_idx + num_len + 1]):
            # print(line[num_idx - 1 : num_idx + num_len + 1])
            return int(num)
            
        if any(c in special_characters for c in above_line[num_idx - 1 : num_idx + num_len + 1]):
            # print(above_line[num_idx - 1 : num_idx + num_len + 1])
            return int(num)
    return 'Not correct'




with open("day3.txt") as f:
    lines = f.readlines()
    corrected_nums = []

    for line_idx in range(len(lines)):

        line = lines[line_idx]

        nums = get_num(line)
        # print(line, '\n', nums)
        
        if line_idx == 0:
            # print(line_idx, "hey first line")
            below_line = lines[line_idx + 1]
            
            
            for num in sorted(nums,reverse=True):
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]
                # print(num, num_idxs)
                s = '.'*len(num)
                line = line.replace(num,s)

                for num_idx in num_idxs:
                    correct_num = check_special_char_first_line(num, num_idx, line, below_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)



        if line_idx == len(lines) - 1:
            # print(line_idx, "hey last line")
            above_line = lines[line_idx - 1]

            for num in sorted(nums, reverse=True):
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]
                # print(num, num_idxs)
                s = '.'*len(num)
                line = line.replace(num,s)

                for num_idx in num_idxs:
                    correct_num = check_special_char_last_line(num, num_idx, line, above_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)


        if line_idx > 0 and line_idx < len(lines) - 1:
            # print(line_idx, "hey middle line")
            above_line = lines[line_idx - 1]
            below_line = lines[line_idx + 1]

            for num in sorted(nums, reverse=True):
                num_idxs = [index for index in range(len(line)) if line.startswith(num, index)]
                s = '.'*len(num)
                line = line.replace(num,s)
                # print(num, num_idxs)
                
                for num_idx in num_idxs:
                    correct_num = check_special_char_middle_line(num, num_idx, line, above_line, below_line)
                    if type(correct_num) == int:
                        corrected_nums.append(correct_num)

        

    print(corrected_nums, sum(corrected_nums))
    # print(lines[139])
                            


