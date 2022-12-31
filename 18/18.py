from collections import deque

# Part 1
with open(r'/home/macolella/AoC2022/18/input') as f:
    scanner = f.read().splitlines()

surface_area = 6*len(scanner)
for ind, block in enumerate(scanner):
    x, y, z = block.split(',')
    scanner[ind] = (int(x), int(y), int(z))

for ind, block1 in enumerate(scanner):
    scanner_excluded = scanner[:ind] + scanner[ind + 1:]
    for block2 in scanner_excluded:
        if abs(block1[0] - block2[0]) + abs(block1[1] - block2[1]) + abs(block1[2] - block2[2]) == 1:
            surface_area -= 1

print(f'The answer to Part 1 is {surface_area}')

# Part 2
min_x = min([block[0] for block in scanner]) - 1
min_y = min([block[1] for block in scanner]) - 1
min_z = min([block[2] for block in scanner]) - 1
max_x = max([block[0] for block in scanner]) + 1
max_y = max([block[1] for block in scanner]) + 1
max_z = max([block[2] for block in scanner]) + 1
scanner_min = [min_x, min_y, min_z]
dirs = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

def bfs(start):
    q = deque()
    seen = set()
    ext_surf = set()
    surface_area = 0
    q.append([start])
    while q:
        path = q.popleft()
        x, y, z = path[-1]
        if (x, y, z) not in seen:
            seen.add((x, y, z))
            for dir_x, dir_y, dir_z in dirs:
                new_x, new_y, new_z = x + dir_x, y + dir_y, z + dir_z
                if min_x <= new_x <= max_x and min_y <= new_y <= max_y and min_z <= new_z <= max_z:
                    if (new_x, new_y, new_z) in scanner:
                        ext_surf.add((new_x, new_y, new_z))
                        surface_area += 1
                    if (new_x, new_y, new_z) not in ext_surf:
                        path_copy = path[:]
                        path_copy.append((new_x, new_y, new_z))
                        q.append(path_copy)
    return surface_area

print(f'The answer to Part 2 is {bfs(scanner_min)}')