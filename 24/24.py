from collections import deque

# Part 1
with open(r'/home/macolella/AoC2022/24/input') as f:
    snow_map = f.read().splitlines()

# Get start/end coords in the snow map
for ind, char in enumerate(snow_map[0]):
    if char == '.':
        start = (0, ind)

for ind, char in enumerate(snow_map[-1]):
    if char == '.':
        end = (len(snow_map) - 1, ind)

# Get wall coords
walls = set()
for ind_row, row in enumerate(snow_map):
    for ind_col, char in enumerate(row):
        if char == '#':
            walls.add((ind_row, ind_col))
walls.add((start[0] - 1, start[1]))
walls.add((end[0] + 1, end[1]))

# Generate new snow map every timestep
height = len(snow_map) - 2
width = len(snow_map[0]) - 2
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
timestep = 0
left_blizzes = set()
right_blizzes = set()
up_blizzes = set()
down_blizzes = set()
for ind_row, row in enumerate(snow_map):
    for ind_col, char in enumerate(row):
        if char == '<':
            left_blizzes.add((ind_row, ind_col))
        elif char == '>':
            right_blizzes.add((ind_row, ind_col))
        elif char == '^':
            up_blizzes.add((ind_row, ind_col))
        elif char == 'v':
            down_blizzes.add((ind_row, ind_col))

def gen_walls(timestep):
    left_blizzes_new = {(row, (col - timestep + width - 1) % (width) + 1) for row, col in left_blizzes}
    right_blizzes_new = {(row, (col + timestep - 1) % (width) + 1) for row, col in right_blizzes}
    up_blizzes_new = {((row - timestep + height - 1) % (height) + 1, col) for row, col in up_blizzes}
    down_blizzes_new = {((row + timestep - 1) % (height) + 1, col) for row, col in down_blizzes}
    return left_blizzes_new | right_blizzes_new | up_blizzes_new | down_blizzes_new | walls

# BFS through maze
def bfs(start, end, timestep):
    q = deque()
    visited_states = set()
    q.append([(start[0], start[1], timestep)])
    while q:
        path = q.popleft()
        row, col, timestep_current = path[-1]
        if (row, col, timestep_current) not in visited_states:
            visited_states.add((row, col, timestep_current))
            if (row, col) == end:
                return timestep_current
            walls_all = gen_walls(timestep_current + 1 % 600)
            for dir_row, dir_col in dirs:
                new_row, new_col = row + dir_row, col + dir_col
                if (new_row, new_col) not in walls_all:
                    path_copy = path[:]
                    path_copy.append((new_row, new_col, timestep_current + 1))
                    q.append(path_copy)

lap1 = bfs(start, end, timestep)
print(f'The answer to Part 1 is {lap1}')

# Part 2
lap2 = bfs(end, start, lap1)
lap3 = bfs(start, end, lap2)
print(f'The answer to Part 2 is {lap3}')