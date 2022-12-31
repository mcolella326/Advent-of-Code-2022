import string
import re

#Part 1
priority_dict = dict()
for letter, priority in zip([*string.ascii_letters], range(1,53)):
    priority_dict[letter] = priority

with open(r'./input') as f:
    sacks = f.read().splitlines()

sacks_1 = [[sack[:len(sack)//2] + ' ' + sack[len(sack)//2:]] for sack in sacks]

common = []
for sack in sacks_1:
    result = re.match(r'.*(\w).*\s.*\1.*', str(sack))
    common.append(result.group(1))

priority_sum = 0
for letter in common:
    priority_sum += priority_dict[letter]

print(f'The answer to Part 1 is {priority_sum}')

#Part 2
counter = 0
entry = 0
sacks_2 = ['']
for sack in sacks:
    if counter < 2:
        sacks_2[entry] += sack + ' '
        counter += 1
    else:
        sacks_2[entry] += sack
        sacks_2.append('')
        counter = 0
        entry += 1
sacks_2.pop()

common = []
for sack in sacks_2:
    result = re.match(r'.*(\w).*\s.*\1.*\s.*\1.*', str(sack))
    common.append(result.group(1))

priority_sum = 0
for letter in common:
    priority_sum += priority_dict[letter]

print(f'The answer to Part 2 is {priority_sum}')