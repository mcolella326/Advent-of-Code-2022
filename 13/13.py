import re
import json
from itertools import zip_longest

# Part 1
with open(r'/home/macolella/AoC2022/13/input') as f:
    packets = f.read().split('\n\n')

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b: 
            return True
        elif a > b: 
            return False
        else:
            pass
 
    elif isinstance(a, list) and isinstance(b, list):
        pairs = zip_longest(a, b)
        for pair in pairs:
            if pair[0] == None: 
                return True
            elif pair[1] == None: 
                return False
            else:
                res = compare(pair[0], pair[1])
                if res != None:
                    return res

    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
        
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

right_order = []
index = 1
for line in packets:
    line = line.split('\n')
    line[0], line[1] = json.loads(line[0]), json.loads(line[1])
    if compare(line[0], line[1]):
        right_order.append(index)
    index += 1

print(f'The answer to Part 1 is {sum(right_order)}')

# Part 2
packets = [line.split('\n') for line in packets]
packets = [line for sublist in packets for line in sublist]
packets = [json.loads(line) for line in packets[:-1]]
packets.append([[2]])
packets.append([[6]])

def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if not compare(elements[i], elements[i + 1]):
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]       
        if not swapped:
            return
 
bubblesort(packets)
index1 = packets.index([[2]]) + 1
index2 = packets.index([[6]]) + 1
print(f'The answer to Part 2 is {index1*index2}')