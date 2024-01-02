def read_file(filename):
    with open(filename) as f:
        lines = f.read().split(',')
    return lines


def hash(chars):
    cur_value = 0
    for char in chars:
        cur_value = ((cur_value + ord(char)) * 17 ) % 256
    return cur_value - 1

def is_exist(input_label, row):
    for id, (label, _) in enumerate(row):
        if input_label == label:
            return id
    return -1
    




def main():
    
    lines = read_file('day15.txt')
    buckets = [[] for _ in range(255)]     

    for line in lines:
        if line.find('=') != -1:
            input_label = line.split('=')[0]
            focal_length = line.split('=')[1]
            if focal_length == '':
                focal_length = 0

            box_order = hash(input_label)
            idx = is_exist(input_label, buckets[box_order])
            if idx  > -1:
                buckets[box_order][idx] = input_label, focal_length
            else:
                buckets[box_order].append((input_label, focal_length))

                
        else:
            input_label = line.split('-')[0]
            focal_length = line.split('-')[1]
            if focal_length == '':
                focal_length = 0
            box_order = hash(input_label)
            idx = is_exist(input_label, buckets[box_order])
            # print(idx)
            if idx  > -1:
                del buckets[box_order][idx]
            
    
    print(buckets)



if __name__ == "__main__":
    main()