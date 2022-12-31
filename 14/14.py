import numpy as np

# Part 1
with open(r'/home/macolella/AoC2022/14/input') as f:
    rock_positions = f.read().splitlines()

rock_positions = [position.split(' -> ') for position in rock_positions]

# Bounding section pass
widths = []
depths = []
for lines in rock_positions:
    for coord_str in lines:
        widths.append(int(coord_str.split(',')[0]))
        depths.append(int(coord_str.split(',')[1]))

cavern_section = np.chararray([max(depths) + 2,max(widths) - min(widths) + 2], unicode=1)
cavern_section[:] = '.'
shift_factor = min(widths)
sand_coords = [0, 500 - shift_factor]
max_depth = 0

# Rock locating pass
for lines in rock_positions:
    x = []
    y = []
    for coord_str in lines:
        coord_str = coord_str.split(',')
        x.append(int(coord_str[0]) - shift_factor) 
        y.append(int(coord_str[1]))
        if int(coord_str[1]) > max_depth:
            max_depth = int(coord_str[1])
    for ind in range(len(x) - 1):
        if x[ind] - x[ind + 1] == 0:
            cavern_section[y[ind]:y[ind + 1] + 1, x[ind]] = '#'
            cavern_section[y[ind + 1]:y[ind] + 1, x[ind]] = '#' 
        elif y[ind] - y[ind + 1] == 0:
            cavern_section[y[ind], x[ind]:x[ind + 1] + 1] = '#'
            cavern_section[y[ind], x[ind + 1]:x[ind] + 1] = '#'

# Sand simulation
max_sand_depth = sand_coords[0]
num_particles = 0
while max_sand_depth < max_depth:
    if cavern_section[sand_coords[0] + 1, sand_coords[1]] == '.':
        sand_coords[0] += 1
        max_sand_depth += 1
    elif cavern_section[sand_coords[0] + 1, sand_coords[1] - 1] == '.':
        sand_coords[0] += 1
        sand_coords[1] -= 1
        max_sand_depth += 1
    elif cavern_section[sand_coords[0] + 1, sand_coords[1] + 1] == '.':
        sand_coords[0] += 1
        sand_coords[1] += 1
        max_sand_depth += 1
    else:
        cavern_section[sand_coords[0], sand_coords[1]] = 'o'
        sand_coords = [0, 500 - shift_factor]
        max_sand_depth = sand_coords[0]
        num_particles += 1

print(f'The answer to Part 1 is {num_particles}')

# Part 2
cavern_section = np.chararray([max(depths) + 3,max(widths) - min(widths) + 250], unicode=1)
cavern_section[:] = '.'
shift_factor = min(widths)
sand_coords = [0, 500 - shift_factor]
max_depth = 0

# Rock locating pass
cavern_section[max(depths) + 2, :] = '#'
for lines in rock_positions:
    x = []
    y = []
    for coord_str in lines:
        coord_str = coord_str.split(',')
        x.append(int(coord_str[0]) - shift_factor) 
        y.append(int(coord_str[1]))
        if int(coord_str[1]) > max_depth:
            max_depth = int(coord_str[1])
    for ind in range(len(x) - 1):
        if x[ind] - x[ind + 1] == 0:
            cavern_section[y[ind]:y[ind + 1] + 1, x[ind]] = '#'
            cavern_section[y[ind + 1]:y[ind] + 1, x[ind]] = '#' 
        elif y[ind] - y[ind + 1] == 0:
            cavern_section[y[ind], x[ind]:x[ind + 1] + 1] = '#'
            cavern_section[y[ind], x[ind + 1]:x[ind] + 1] = '#'

# Sand simulation
max_sand_depth = sand_coords[0]
num_particles = 0
while cavern_section[0, 500 - shift_factor] == '.':
    if cavern_section[sand_coords[0] + 1, sand_coords[1]] == '.':
        sand_coords[0] += 1
        max_sand_depth += 1
    elif cavern_section[sand_coords[0] + 1, sand_coords[1] - 1] == '.':
        sand_coords[0] += 1
        sand_coords[1] -= 1
        max_sand_depth += 1
    elif cavern_section[sand_coords[0] + 1, sand_coords[1] + 1] == '.':
        sand_coords[0] += 1
        sand_coords[1] += 1
        max_sand_depth += 1
    else:
        cavern_section[sand_coords[0], sand_coords[1]] = 'o'
        sand_coords = [0, 500 - shift_factor]
        max_sand_depth = sand_coords[0]
        num_particles += 1

print(f'The answer to Part 2 is {num_particles}')