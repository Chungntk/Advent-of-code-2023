with open("day2.txt") as f:
    lines = f.readlines()
    game_ids = []
    game_power = []
    for line in lines:
        id = line[line.find('Game ') + 5 : line.find(':')]
        
        sets = line[line.find(':') + 2 : ].split('; ')
        sets_cnt = 0
        for set in sets:

            cubes = set.split(', ')
            cube_cnt = 0

            for cube in cubes:
                cube_info = cube.split()
                if cube_info[1] == 'blue' and int(cube_info[0]) <= 14:
                    cube_cnt += 1
                if cube_info[1] == 'red' and int(cube_info[0]) <= 12:
                    cube_cnt += 1
                if cube_info[1] == 'green' and int(cube_info[0]) <= 13:
                    cube_cnt += 1

            if cube_cnt == len(cubes):
                sets_cnt += 1
        if sets_cnt == len(sets):
            game_ids.append(int(id))

    print(sum(game_ids))

# Part 2
    for line in lines:
        id = line[line.find('Game ') + 5 : line.find(':')]
        
        sets = line[line.find(':') + 2 : ].split('; ')
        max_blue = 0
        max_green = 0
        max_red = 0

        for set in sets:

            cubes = set.split(', ')
            cube_cnt = 0

            for cube in cubes:
                cube_info = cube.split()
                if cube_info[1] == 'blue' and int(cube_info[0]) >= max_blue:
                    max_blue = int(cube_info[0])
                if cube_info[1] == 'red' and int(cube_info[0]) >= max_red:
                    max_red = int(cube_info[0])
                if cube_info[1] == 'green' and int(cube_info[0]) >= max_green:
                    max_green = int(cube_info[0])

        game_power.append(max_blue * max_red * max_green)
    
    print(sum(game_power))