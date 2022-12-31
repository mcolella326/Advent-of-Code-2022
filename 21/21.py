import re

with open(r'/home/macolella/AoC2022/21/input') as f:
    monkey_ops = f.read().splitlines()

# Part 1

# Parsing pass
monkey_dict = {}
for op in monkey_ops:
    if op_re := re.match(r'(.*): (\d+)', op):
        monkey = op_re.group(1)
        num = op_re.group(2)
        monkey_dict[monkey] = num
    elif op_re := re.match(r'(.*): (.*)', op):
        monkey = op_re.group(1)
        operation = op_re.group(2)
        monkey_dict[monkey] = operation

# Solving pass
def parse(monkey_dict, monkey):
    if monkey_dict[monkey].isdigit():
        return int(monkey_dict[monkey])
    else:
        exp_re = re.match(r'(.*) (.) (.*)', monkey_dict[monkey])
        monkey1 = exp_re.group(1)
        operation = exp_re.group(2)
        monkey2 = exp_re.group(3)
        if operation == '+':
            return parse(monkey_dict, monkey1) + parse(monkey_dict, monkey2)
        elif operation == '-':
            return parse(monkey_dict, monkey1) - parse(monkey_dict, monkey2)
        elif operation == '*':
            return parse(monkey_dict, monkey1) * parse(monkey_dict, monkey2)
        elif operation == '/':
            return parse(monkey_dict, monkey1) / parse(monkey_dict, monkey2)

print(f'The answer to Part 1 is {int(parse(monkey_dict, "root"))}')

# Part 2
test_int = 0
monkey_dict['humn'] = str(test_int)
exp_re = re.match(r'(.*) . (.*)', monkey_dict['root'])
monkey1 = exp_re.group(1)
monkey2 = exp_re.group(2)
cons = parse(monkey_dict, monkey2)

for _ in range(10_000):
    dint = 1
    monkey_dict['humn'] = str(test_int)
    func = parse(monkey_dict, monkey1) - cons
    monkey_dict['humn'] = str(test_int + dint)
    func_plus_one = parse(monkey_dict, monkey1) - cons
    test_int = int(test_int - (func*dint)/(func_plus_one - func))
    if abs(func) < 1:
        break

print(f'The answer to Part 2 is {round(test_int)}')