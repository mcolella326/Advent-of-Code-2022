import numpy as np

# Part 1
with open(r'./input') as f:
    input = f.read().splitlines()

input = [[num for num in line] for line in input]

length = len(input[0])
height = len(input)
tree_map = np.empty([length, height])

for row in range(length):
    for col in range(height):
        tree_map[row][col] = input[row][col]

visibility_map = np.full([length, height], True)

for row in range(1, length - 1):
    for col in range(1, height - 1):
        if ((tree_map[row, col] <= max(tree_map[row, :col])) and
                (tree_map[row, col] <= max(tree_map[row, col + 1:])) and
                (tree_map[row, col] <= max(tree_map[:row, col])) and
                (tree_map[row, col] <= max(tree_map[row + 1:, col]))):
            visibility_map[row, col] = False

print(f'The answer to Part 1 is {np.count_nonzero(visibility_map)}')

# Part 2
scenic_score = []
for row in range(1, length - 1):
    for col in range(1, height - 1):
        # Look left
        if (tree_map[row, col] <= max(tree_map[row, :col])):
            left_look = np.flipud(tree_map[row, :col])
            index = np.nonzero(tree_map[row, col] <= left_look)[0][0]
            scenic_l = index + 1
        else:
            scenic_l = len(tree_map[row, :col])
        # Look right
        if (tree_map[row, col] <= max(tree_map[row, col + 1:])):
            right_look = tree_map[row, col + 1:]
            index = np.nonzero(tree_map[row, col] <= right_look)[0][0]
            scenic_r = index + 1
        else:
            scenic_r = len(tree_map[row, col + 1:])
        # Look up
        if (tree_map[row, col] <= max(tree_map[:row, col])):
            up_look = np.flipud(tree_map[:row, col])
            index = np.nonzero(tree_map[row, col] <= up_look)[0][0]
            scenic_u = index + 1
        else:
            scenic_u = len(tree_map[:row, col])
        # Look down
        if (tree_map[row, col] <= max(tree_map[row + 1:, col])):
            down_look = tree_map[row + 1:, col]
            index = np.nonzero(tree_map[row, col] <= down_look)[0][0]
            scenic_d = index + 1
        else:
            scenic_d = len(tree_map[row + 1:, col])
        
        scenic_score.append(scenic_u*scenic_d*scenic_l*scenic_r)

print(f'The answer to Part 2 is {max(scenic_score)}')
