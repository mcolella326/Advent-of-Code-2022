# Part 1
with open(r'./input') as f:
    movements = f.read().splitlines()

movements = [move.split() for move in movements]

head = [25, 25]
tail = [25, 25]
tail_visited = set()
tail_visited.add(tuple(tail))

def tail_follower(h, t):
    # Cardinal movement ONLY
    # Left
    if (h[1] == t[1] - 2) and (h[0] == t[0]):
        t[1] -= 1
    # Right
    elif (h[1] == t[1] + 2) and (h[0] == t[0]):
        t[1] += 1
    # Up
    elif (h[0] == t[0] + 2) and (h[1] == t[1]):
        t[0] += 1
    # Down
    elif (h[0] == t[0] - 2) and (h[1] == t[1]):
        t[0] -= 1
    # Diagonal movement ONLY
    # Up Right
    elif (((h[0] == t[0] + 1) and (h[1] == t[1] + 2)) or 
            ((h[0] == t[0] + 2) and (h[1] == t[1] + 1)) or 
            ((h[0] == t[0] + 2) and (h[1] == t[1] + 2))):
        t[0] += 1
        t[1] += 1
    # Down Right
    elif (((h[0] == t[0] - 1) and (h[1] == t[1] + 2)) or 
            ((h[0] == t[0] - 2) and (h[1] == t[1] + 1)) or 
            ((h[0] == t[0] - 2) and (h[1] == t[1] + 2))):
        t[0] -= 1
        t[1] += 1
    # Down Left
    elif (((h[0] == t[0] - 1) and (h[1] == t[1] - 2)) or 
            ((h[0] == t[0] - 2) and (h[1] == t[1] - 1)) or 
            ((h[0] == t[0] - 2) and (h[1] == t[1] - 2))):
        t[0] -= 1
        t[1] -= 1
    # Up Left
    elif (((h[0] == t[0] + 1) and (h[1] == t[1] - 2)) or 
            ((h[0] == t[0] + 2) and (h[1] == t[1] - 1)) or 
            ((h[0] == t[0] + 2) and (h[1] == t[1] - 2))):
        t[0] += 1
        t[1] -= 1
    return t

def move_tail(tail):
    tail = tail_follower(head, tail)
    tail_visited.add(tuple(tail))
    return

for move in movements:
    direction = move[0]
    num_spaces = int(move[1])
    if direction == 'L':
        for _ in range(num_spaces):
            head[1] -= 1
            move_tail(tail)
    elif direction == 'R':
        for _ in range(num_spaces):
            head[1] += 1
            move_tail(tail)
    elif direction == 'U':
        for _ in range(num_spaces):
            head[0] += 1
            move_tail(tail)
    elif direction == 'D':
        for _ in range(num_spaces):
            head[0] -= 1
            move_tail(tail)

print(f'The answer to Part 1 is {len(tail_visited)}')

# Part 2
head = [25, 25]
tail_intermediate1 = [25, 25]
tail_intermediate2 = [25, 25]
tail_intermediate3 = [25, 25]
tail_intermediate4 = [25, 25]
tail_intermediate5 = [25, 25]
tail_intermediate6 = [25, 25]
tail_intermediate7 = [25, 25]
tail_intermediate8 = [25, 25]
tail_intermediate9 = [25, 25]
tail_visited = set()
tail_visited.add(tuple(tail_intermediate9))

def move_tail_repeatedly(head, tail_intermediate1, tail_intermediate2, 
        tail_intermediate3, tail_intermediate4, tail_intermediate5, 
        tail_intermediate6, tail_intermediate7, tail_intermediate8, tail_intermediate9):
    tail_intermediate1 = tail_follower(head, tail_intermediate1)
    tail_intermediate2 = tail_follower(tail_intermediate1, tail_intermediate2)
    tail_intermediate3 = tail_follower(tail_intermediate2, tail_intermediate3)
    tail_intermediate4 = tail_follower(tail_intermediate3, tail_intermediate4)
    tail_intermediate5 = tail_follower(tail_intermediate4, tail_intermediate5)
    tail_intermediate6 = tail_follower(tail_intermediate5, tail_intermediate6)
    tail_intermediate7 = tail_follower(tail_intermediate6, tail_intermediate7)
    tail_intermediate8 = tail_follower(tail_intermediate7, tail_intermediate8)
    tail_intermediate9 = tail_follower(tail_intermediate8, tail_intermediate9)
    tail_visited.add(tuple(tail_intermediate9))
    return

for move in movements:
    direction = move[0]
    num_spaces = int(move[1])
    if direction == 'L':
        for _ in range(num_spaces):
            head[1] -= 1
            move_tail_repeatedly(head, tail_intermediate1, tail_intermediate2, 
                tail_intermediate3, tail_intermediate4, tail_intermediate5, 
                tail_intermediate6, tail_intermediate7, tail_intermediate8, tail_intermediate9)
    elif direction == 'R':
        for _ in range(num_spaces):
            head[1] += 1
            move_tail_repeatedly(head, tail_intermediate1, tail_intermediate2, 
                tail_intermediate3, tail_intermediate4, tail_intermediate5, 
                tail_intermediate6, tail_intermediate7, tail_intermediate8, tail_intermediate9)
    elif direction == 'U':
        for _ in range(num_spaces):
            head[0] += 1
            move_tail_repeatedly(head, tail_intermediate1, tail_intermediate2, 
                tail_intermediate3, tail_intermediate4, tail_intermediate5, 
                tail_intermediate6, tail_intermediate7, tail_intermediate8, tail_intermediate9)
    elif direction == 'D':
        for _ in range(num_spaces):
            head[0] -= 1
            move_tail_repeatedly(head, tail_intermediate1, tail_intermediate2, 
                tail_intermediate3, tail_intermediate4, tail_intermediate5, 
                tail_intermediate6, tail_intermediate7, tail_intermediate8, tail_intermediate9)

print(f'The answer to Part 2 is {len(tail_visited)}')