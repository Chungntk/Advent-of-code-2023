def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open("day1.txt") as f:
    lines = f.readlines()
    numbers = []
    digits = []
    for line in lines:
        for s in str(line):
            if s.isnumeric() == True:
                digits.append(s)
        
        if len(digits) == 1:
            numbers.append(int(digits[0]+digits[0]))
        if len(digits) == 2:
            numbers.append(int(''.join(digits)))
        if len(digits) > 2:
            numbers.append(int(digits[0] + digits[-1]))
        digits = []
        continue
    
    print(
        sum(numbers)
    )

    numbers_p2 = []
    digits_p2 = []
    for line in lines:
        for i in range(len(line)):
            if line[i].isnumeric() == True:
                ind, temp = i, int(line[i])
                digits_p2.append((i, temp))

            if line.startswith('one', i):
                ind, temp = i, 1
                digits_p2.append((i, temp))

            if line.startswith('two', i):
                ind, temp = i, 2
                digits_p2.append((i, temp))

            if line.startswith('three', i):
                ind, temp = i, 3
                digits_p2.append((i, temp))
            
            if line.startswith('four', i):
                ind, temp = i, 4
                digits_p2.append((i, temp))

            if line.startswith('five', i):
                ind, temp = i, 5
                digits_p2.append((i, temp))

            if line.startswith('six', i):
                ind, temp = i, 6
                digits_p2.append((i, temp))

            if line.startswith('seven', i):
                ind, temp = i, 7
                digits_p2.append((i, temp))

            if line.startswith('eight', i):
                ind, temp = i, 8
                digits_p2.append((i, temp))
            
            if line.startswith('nine', i):
                ind, temp = i, 9
                digits_p2.append((i, temp))
        
        sort_digits_p2 = sorted(digits_p2)
        number = int(str(sort_digits_p2[0][1]) + str(sort_digits_p2[-1][1]))
        numbers_p2.append(number)
        digits_p2 = []

    print(sum(numbers_p2))