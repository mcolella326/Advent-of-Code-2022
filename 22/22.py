import re

with open(r'/home/macolella/AoC2022/22/input') as f:
    flat_map, instructions = f.read().split('\n\n')

# Part 1
flat_map = flat_map.splitlines()

movable_spaces = set()
walls = set()

for row_ind, row in enumerate(flat_map):
    for col_ind, char in enumerate(row):
        if char == '.':
            movable_spaces.add((row_ind, col_ind))
        elif char == '#':
            walls.add((row_ind, col_ind))

fwds = list(map(int, re.findall(r'(\d+)', instructions)))
rotates = re.findall(r'(L|R)', instructions)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 0: right, 1: down, 2: left, 3: up

dir_ind = 0
map_space = movable_spaces | walls
current_pos = min(movable_spaces)

for movement_ind, movement in enumerate(fwds):
    # Movement phase
    if dir_ind == 0 or dir_ind == 2:
        movable_edge_r = max([(row, col) for row, col in map_space if row == current_pos[0]])
        movable_edge_l = min([(row, col) for row, col in map_space if row == current_pos[0]])
        for _ in range(movement):
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if movable_edge_l <= potential_new_pos <= movable_edge_r:
                    current_pos = potential_new_pos
                elif potential_new_pos > movable_edge_r:
                    if movable_edge_l not in walls:
                        current_pos = movable_edge_l
                    else:
                        break
                elif potential_new_pos < movable_edge_l:
                    if movable_edge_r not in walls:
                        current_pos = movable_edge_r
                    else:
                        break
            else:
                break
    elif dir_ind == 1 or dir_ind == 3:
        movable_edge_d = max([(row, col) for row, col in map_space if col == current_pos[1]])
        movable_edge_u = min([(row, col) for row, col in map_space if col == current_pos[1]])
        for _ in range(movement):
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if movable_edge_u <= potential_new_pos <= movable_edge_d:
                    current_pos = potential_new_pos
                elif potential_new_pos > movable_edge_d:
                    if movable_edge_u not in walls:
                        current_pos = movable_edge_u
                    else:
                        break
                elif potential_new_pos < movable_edge_u:
                    if movable_edge_d not in walls:
                        current_pos = movable_edge_d
                    else:
                        break
            else:
                break

    # Rotation phase
    if movement_ind == len(rotates):
        dir_ind %= len(dirs)
        break
    if rotates[movement_ind] == 'R':
        dir_ind = (dir_ind + 1) % len(dirs)
    elif rotates[movement_ind] == 'L':
        dir_ind = (dir_ind - 1) % len(dirs)

print(f'The answer to Part 1 is {1000*(current_pos[0] + 1) + 4*(current_pos[1] + 1) + dir_ind}')

# Part 2
region1_upper_edge = {(-1, col) for col in range(100, 150)}
region1_right_edge = {(row, 150) for row in range(0, 50)}
region1_lower_edge = {(50, col) for col in range(100, 150)}
region2_upper_edge = {(-1, col) for col in range(50, 100)}
region2_left_edge = {(row, 49) for row in range(0, 50)}
region3_left_edge = {(row, 49) for row in range(50, 100)}
region3_right_edge = {(row, 100) for row in range(50, 100)}
region4_right_edge = {(row, 100) for row in range(100, 150)}
region4_lower_edge = {(150, col) for col in range(50, 100)}
region5_upper_edge = {(99, col) for col in range(0, 50)}
region5_left_edge = {(row, -1) for row in range(100, 150)}
region6_left_edge = {(row, -1) for row in range(150, 200)}
region6_lower_edge = {(200, col) for col in range(0, 50)}
region6_right_edge = {(row, 50) for row in range(150, 200)}

dir_ind = 0
current_pos = min(movable_spaces)

for movement_ind, movement in enumerate(fwds):
    # Movement phase
    for _ in range(movement):
        if dir_ind == 0:
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if potential_new_pos not in region1_right_edge | region3_right_edge | region4_right_edge | region6_right_edge:
                    current_pos = potential_new_pos
                elif potential_new_pos in region1_right_edge:
                    potential_new_pos = (-potential_new_pos[0] + 149, 99)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 2
                    else:
                        break
                elif potential_new_pos in region3_right_edge:
                    potential_new_pos = (49, potential_new_pos[0] + 50)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 3
                    else:
                        break
                elif potential_new_pos in region4_right_edge:
                    potential_new_pos = (-potential_new_pos[0] + 149, 149)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 2
                    else:
                        break
                elif potential_new_pos in region6_right_edge:
                    potential_new_pos = (149, potential_new_pos[0] - 100)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 3
                    else:
                        break
            else:
                break
        elif dir_ind == 1:
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if potential_new_pos not in region1_lower_edge | region4_lower_edge | region6_lower_edge:
                    current_pos = potential_new_pos
                elif potential_new_pos in region1_lower_edge:
                    potential_new_pos = (potential_new_pos[1] - 50, 99)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 2
                    else:
                        break
                elif potential_new_pos in region4_lower_edge:
                    potential_new_pos = (potential_new_pos[1] + 100, 49)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 2
                    else:
                        break
                elif potential_new_pos in region6_lower_edge:
                    potential_new_pos = (0, potential_new_pos[1] + 100)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 1
                    else:
                        break
            else:
                break
        elif dir_ind == 2:
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if potential_new_pos not in region2_left_edge | region3_left_edge | region5_left_edge | region6_left_edge:
                    current_pos = potential_new_pos
                elif potential_new_pos in region2_left_edge:
                    potential_new_pos = (-potential_new_pos[0] + 149, 0)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 0
                    else:
                        break
                elif potential_new_pos in region3_left_edge:
                    potential_new_pos = (100, potential_new_pos[0] - 50)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 1
                    else:
                        break
                elif potential_new_pos in region5_left_edge:
                    potential_new_pos = (-potential_new_pos[0] + 149, 50)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 0
                    else:
                        break
                elif potential_new_pos in region6_left_edge:
                    potential_new_pos = (0, potential_new_pos[0] - 100)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 1
                    else:
                        break
            else:
                break
        elif dir_ind == 3:
            potential_new_pos = (current_pos[0] + dirs[dir_ind][0], current_pos[1] + dirs[dir_ind][1])
            if potential_new_pos not in walls:
                if potential_new_pos not in region1_upper_edge | region2_upper_edge | region5_upper_edge:
                    current_pos = potential_new_pos
                elif potential_new_pos in region1_upper_edge:
                    potential_new_pos = (199, potential_new_pos[1] - 100)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 3
                    else:
                        break
                elif potential_new_pos in region2_upper_edge:
                    potential_new_pos = (potential_new_pos[1] + 100, 0)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 0
                    else:
                        break
                elif potential_new_pos in region5_upper_edge:
                    potential_new_pos = (potential_new_pos[1] + 50, 50)
                    if potential_new_pos not in walls:
                        current_pos = potential_new_pos
                        dir_ind = 0
                    else:
                        break
            else:
                break

    # Rotation phase
    if movement_ind == len(rotates):
        dir_ind %= len(dirs)
        break
    if rotates[movement_ind] == 'R':
        dir_ind = (dir_ind + 1) % len(dirs)
    elif rotates[movement_ind] == 'L':
        dir_ind = (dir_ind - 1) % len(dirs)

print(f'The answer to Part 2 is {1000*(current_pos[0] + 1) + 4*(current_pos[1] + 1) + dir_ind}')