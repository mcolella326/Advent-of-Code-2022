import re

# Part 1
with open(r'/home/macolella/AoC2022/17/input') as f:
    jet_pat = f.read()

# jet_pat = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''

def get_rock(rock_num, y):
    if rock_num == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif rock_num == 1:
        return set([(2, y + 1), (3, y), (3, y + 1), (3, y + 2), (4, y + 1)])
    elif rock_num == 2:
        return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
    elif rock_num == 3:
        return set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)])
    elif rock_num == 4:
        return set([(2, y), (2, y + 1), (3, y), (3, y + 1)])

def move_left(rock):
    if any([x == 0 for (x, y) in rock]):
        return rock
    return set([(x - 1, y) for (x, y) in rock])

def move_right(rock):
    if any([x == 6 for (x, y) in rock]):
        return rock
    return set([(x + 1, y) for (x, y) in rock])

def move_up(rock):
    return set([(x, y + 1) for (x, y) in rock])

def move_down(rock):
    return set([(x, y - 1) for (x, y) in rock])

def get_top(stationary_rocks):
    return max([y for (x, y) in stationary_rocks])

stationary_rocks = set()
ground = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
top = 0
jet_ind = 0
for rock_num in range(2022):
    rock = get_rock(rock_num % 5, top + 4)
    falling = True
    while falling:
        wind_dir = jet_pat[jet_ind]
        if wind_dir == '<':
            rock = move_left(rock)
            if rock & stationary_rocks:
                rock = move_right(rock)
        elif wind_dir == '>':
            rock = move_right(rock)
            if rock & stationary_rocks:
                rock = move_left(rock)
        rock = move_down(rock)
        if ((rock & stationary_rocks) or (rock & ground)):
            rock = move_up(rock)
            stationary_rocks |= rock
            top = get_top(stationary_rocks)
            falling = False
        jet_ind = (jet_ind + 1) % len(jet_pat)

print(f'The answer to Part 1 is {top}')

# Part 2
limit = 1_000_000_000_000
stationary_rocks = set()
previous_conditions = {}
ground = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
top = 0
jet_ind = 0
added = 0
rock_num = 0

def signature(stationary_rocks):
    maxY = max([y for (x, y) in stationary_rocks])
    return frozenset([(x, maxY - y) for (x, y) in stationary_rocks if maxY - y <= 30])

while rock_num < limit:
    rock = get_rock(rock_num % 5, top + 4)
    falling = True
    while falling:
        wind_dir = jet_pat[jet_ind]
        if wind_dir == '<':
            rock = move_left(rock)
            if rock & stationary_rocks:
                rock = move_right(rock)
        elif wind_dir == '>':
            rock = move_right(rock)
            if rock & stationary_rocks:
                rock = move_left(rock)
        rock = move_down(rock)
        if ((rock & stationary_rocks) or (rock & ground)):
            rock = move_up(rock)
            stationary_rocks |= rock
            top = get_top(stationary_rocks)
            timestamp = (jet_ind, rock_num % 5, signature(stationary_rocks))
            if timestamp in previous_conditions:
                former_rock_num, former_top = previous_conditions[timestamp]
                height_change = top - former_top
                rock_num_change = rock_num - former_rock_num
                added_cycles = (limit - rock_num) // rock_num_change
                added += added_cycles * height_change
                rock_num += added_cycles * rock_num_change
            previous_conditions[timestamp] = (rock_num, top)
            falling = False
        jet_ind = (jet_ind + 1) % len(jet_pat)
    rock_num += 1

print(added + top)