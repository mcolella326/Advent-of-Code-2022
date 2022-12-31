import re

#Part 1
with open(r'./input') as f:
    elf_list = f.read()
    elf_list = re.split('\n', elf_list)

total_cal = [0]
elf_num = 0
for cal in elf_list:
    if cal is not '':
        total_cal[elf_num] += int(cal)
    else:
        elf_num += 1
        total_cal.append(0)

print(f'Part 1 answer is {max(total_cal)}')

#Part 2
total_cal = sorted(total_cal)[-3:]
print(f'Part 2 answer is {sum(total_cal)}')