with open("day1.txt") as f:
    lines = f.readlines()
    all = []
    part = []
    for line in lines:
        if line != "\n":
            part.append(int(line[:-1]))
        else:
            s = sum(part)
            all.append(s)
            part = []
            # print(part)
        continue

    all.sort()

    print(
        all,
        "\n Max of the Calories carried by 1 Elves is: \n",
        max(all),
        "\n The sum of the Calories carried by the top three Elves is: \n",
        sum(all[-3:]),
    )