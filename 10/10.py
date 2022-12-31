import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

with open(r'/home/macolella/AoC2022/10/input') as f:
    code = f.read().splitlines()

# Part 1
cycle = 1
x = 1
signal_str = []

def strength_checker(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_str.append(cycle*x)
    return

for line in code:
    if line == 'noop':
        strength_checker(cycle, x)
        cycle += 1
    else:
        num = int(line.split()[1])
        strength_checker(cycle, x)
        cycle += 1
        strength_checker(cycle, x)
        cycle += 1
        x += num

print(f'The answer to Part 1 is {sum(signal_str)}')

# Part 2
cycle = 1
x = 1
row = -1
crt = np.chararray([6,40], unicode=1)
crt[:] = '.'

for line in code:
    if line == 'noop':
        pixel_pos = (cycle - 1) % 40
        if pixel_pos == 0:
            row += 1
        sprite_poses = [x, x-1, x+1]
        if pixel_pos in sprite_poses:
            crt[row][pixel_pos] = '#'
        cycle += 1
    else:
        num = int(line.split()[1])
        pixel_pos = (cycle - 1) % 40
        if pixel_pos == 0:
            row += 1
        sprite_poses = [x, x-1, x+1]
        if pixel_pos in sprite_poses:
            crt[row][pixel_pos] = '#'
        cycle += 1
        pixel_pos = (cycle - 1) % 40
        if pixel_pos == 0:
            row += 1
        if pixel_pos in sprite_poses:
            crt[row][pixel_pos] = '#'
        cycle += 1
        x += num

print(crt)