from collections import deque

with open(r'/home/macolella/AoC2022/12/input') as file:
    grid = [line.strip() for line in file.readlines()]

height_dict = {chr(i): i - 96 for i in range(97, 97+26)}
height_dict['S'] = 1
height_dict['E'] = 26
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i, line in enumerate(grid):
    if 'S' in line:
        j = line.index('S')
        start = (i, j)
    if 'E' in line:
        j = line.index('E')
        end = (i, j)

def bfs(start, end):
    q = deque()
    seen = set()
    q.append([start])
    while q:
        path = q.popleft()
        row, col = path[-1]
        if (row, col) not in seen:
            seen.add((row, col))
            if (row, col) == end:
                return len(path) - 1
            ch = grid[row][col]
            height1 = height_dict[ch]
            for dir_row, dir_col in dirs:
                new_row, new_col = row + dir_row, col + dir_col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    ch = grid[new_row][new_col]
                    height2 = height_dict[ch]
                    if height2 <= height1 + 1:
                        path_copy = path[:]
                        path_copy.append((new_row, new_col))
                        q.append(path_copy)

# Part 1
print(bfs(start, end))

# Part 2
starts = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            starts.add((i, j))
ans = float('inf')
for start in starts:
    dist = bfs(start, end)
    if dist is not None:
        ans = min(ans, dist)
print(ans)