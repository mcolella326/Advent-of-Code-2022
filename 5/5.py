import re

# Part 1
with open(r'./input') as f:
    all_input = f.read().splitlines()

lines = all_input[:8]

columns = []
for line in lines:
    column = []
    for line_index in range(1,35,4):
        column.append(line[line_index])
    columns.append(column) 

stacks = list(zip(*reversed(columns)))

for ind, stack in enumerate(stacks):
    stacks[ind] = [box for box in stack if box.strip()]

# stacks = [
#     [s for s in stack if s.strip()] for stack in stacks
# ]

instructions = all_input[10:]

move_num = 0
stack_from = 0
stack_to = 0
for instruction in instructions:
    matches = re.match(r'move (\d*) from (\d*) to (\d*)', instruction)
    move_num = int(matches.group(1))
    stack_from = int(matches.group(2))
    stack_to = int(matches.group(3))
    for _ in range(move_num):
        moving_box = stacks[stack_from - 1].pop()
        stacks[stack_to - 1].append(moving_box)

first_ans = ''
for stack in stacks:
    first_ans += str(stack[-1])

print(f'The answer to Part 1 is {first_ans}')

# Part 2
stacks = list(zip(*reversed(columns)))

for ind, stack in enumerate(stacks):
    stacks[ind] = [box for box in stack if box.strip()]

for instruction in instructions:
    matches = re.match(r'move (\d*) from (\d*) to (\d*)', instruction)
    move_num = int(matches.group(1))
    stack_from = int(matches.group(2))
    stack_to = int(matches.group(3))
    moving_boxes = stacks[stack_from - 1][-move_num:]
    del stacks[stack_from - 1][-move_num:]
    stacks[stack_to - 1] += moving_boxes

second_ans = ''
for stack in stacks:
    second_ans += str(stack[-1])

print(f'The answer to Part 2 is {second_ans}')