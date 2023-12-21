def read_file(filename):
    with open(filename) as f:
        lines = f.read().split(',')
    return lines


def hash(chars):
    cur_value = 0
    for char in chars:
        cur_value = ((cur_value + ord(char)) * 17 ) % 256
    return cur_value


def main():
    
    lines = read_file('day15.txt')
    # sum_results_part_1 = 0
    
    # for line in lines:
    #     cur_value = hash(line)
    #     sum_results_part_1 = sum_results_part_1 + cur_value
    
    # print(line, sum_results_part_1) 
            
    boxs = {}
    for i in range(255):
        key = i  # You can customize the key format as needed
        value =  i+2, 3  # You can customize the value format as needed
        boxs[key] = value
    
    print(boxs)

    for line in lines:
        print(line)
        if line.find('=') != -1:
            label = line.split('=')[0]
            focal_length = line.split('=')[1]
            box_order = hash(label)
            if box_order in boxs.keys(): 
                boxs[box_order] = label, focal_length
            else:
                
        else:
            label = line.split('-')[0]
            focal_length = line.split('-')[1]
            box_order = hash(label)
            boxs[box_order] = label, focal_length

            box = hash(line.split('-')[0])

    #     print(box)



if __name__ == "__main__":
    main()