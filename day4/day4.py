def read_file(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
    return lines

def get_score(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return get_score(n-1)*2


def main():

    lines = read_file('day4.txt')
    final_score = 0

    for line in lines:
        goal = line.split(': ')[1].split('|')[0].split()
        mine = line.split(': ')[1].split('|')[1].split()
        # score = get_score(4)
        score_cnt = 0
        for m in mine:
            if m in goal:
                print(m)
                score_cnt += 1
        final_score = final_score + get_score(score_cnt)
        print(score_cnt, goal, mine)
    print(final_score)



if __name__ == "__main__":
    main()