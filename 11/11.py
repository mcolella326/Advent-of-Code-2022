import re

# Part 1
with open(r'/home/macolella/AoC2022/11/input') as f:
    monkey_rules = f.read().splitlines()

monkey_dict = dict()
new = 0

# Parsing pass
for line in monkey_rules:
    if (monkey_num_re := re.match(r'Monkey (\d)', line.strip())):
        monkey_num = int(monkey_num_re.group(1))
        monkey_dict[monkey_num] = {}
    elif (starting_items_re := re.match(r'Starting items: (.*)', line.strip())):
        starting_items = starting_items_re.group(1).split(', ')
        starting_items = [int(item) for item in starting_items]
        monkey_dict[monkey_num]['items'] = starting_items
        monkey_dict[monkey_num]['counter'] = 0
    elif (operation_re := re.match(r'Operation: (.*)', line.strip())):
        operation = operation_re.group(1)
        operation += '; new = new // 3'
        monkey_dict[monkey_num]['operation'] = operation
    elif (test_re := re.match('Test: divisible by (\d+)', line.strip())):
        test_num = int(test_re.group(1))
        monkey_dict[monkey_num]['divisibility_test'] = test_num
    elif (true_con_re := re.match(r'If true: throw to monkey (\d)', line.strip())):
        true_con = int(true_con_re.group(1))
        monkey_dict[monkey_num]['true_con'] = true_con
    elif (false_con_re := re.match(r'If false: throw to monkey (\d)', line.strip())):
        false_con = int(false_con_re.group(1))
        monkey_dict[monkey_num]['false_con'] = false_con

# Looping pass
for _ in range(20):
    for line in monkey_rules:
        if (monkey_num_re := re.match(r'Monkey (\d)', line.strip())):
            monkey_num = int(monkey_num_re.group(1))
            for item in monkey_dict[monkey_num]['items']:
                old = item
                exec(monkey_dict[monkey_num]['operation'])
                if (new % monkey_dict[monkey_num]['divisibility_test'] == 0):
                    monkey_dict[monkey_dict[monkey_num]['true_con']]['items'].append(new)
                else:
                    monkey_dict[monkey_dict[monkey_num]['false_con']]['items'].append(new)
            counter = len(monkey_dict[monkey_num]['items'])
            monkey_dict[monkey_num]['counter'] += counter
            del monkey_dict[monkey_num]['items'][:]

counter_list = []
for monkey in monkey_dict.keys():
    counter_list.append(monkey_dict[monkey]['counter'])
monkey_business = sorted(counter_list)[-1] * sorted(counter_list)[-2]

print(f'The answer to Part 1 is {monkey_business}')

# Part 2
monkey_dict = dict()
new = 0

# Parsing pass
for line in monkey_rules:
    if (monkey_num_re := re.match(r'Monkey (\d)', line.strip())):
        monkey_num = int(monkey_num_re.group(1))
        monkey_dict[monkey_num] = {}
    elif (starting_items_re := re.match(r'Starting items: (.*)', line.strip())):
        starting_items = starting_items_re.group(1).split(', ')
        starting_items = [int(item) for item in starting_items]
        monkey_dict[monkey_num]['items'] = starting_items
        monkey_dict[monkey_num]['counter'] = 0
    elif (operation_re := re.match(r'Operation: (.*)', line.strip())):
        operation = operation_re.group(1)
        monkey_dict[monkey_num]['operation'] = operation
    elif (test_re := re.match('Test: divisible by (\d+)', line.strip())):
        test_num = int(test_re.group(1))
        monkey_dict[monkey_num]['divisibility_test'] = test_num
    elif (true_con_re := re.match(r'If true: throw to monkey (\d)', line.strip())):
        true_con = int(true_con_re.group(1))
        monkey_dict[monkey_num]['true_con'] = true_con
    elif (false_con_re := re.match(r'If false: throw to monkey (\d)', line.strip())):
        false_con = int(false_con_re.group(1))
        monkey_dict[monkey_num]['false_con'] = false_con

lcm = 1
for monkey in monkey_dict.keys():
    lcm *= monkey_dict[monkey]['divisibility_test']

# Looping pass
for _ in range(10000):
    for line in monkey_rules:
        if (monkey_num_re := re.match(r'Monkey (\d)', line.strip())):
            monkey_num = int(monkey_num_re.group(1))
            for item in monkey_dict[monkey_num]['items']:
                old = item
                exec(monkey_dict[monkey_num]['operation'])
                new %= lcm
                if (new % monkey_dict[monkey_num]['divisibility_test'] == 0):
                    monkey_dict[monkey_dict[monkey_num]['true_con']]['items'].append(new)
                else:
                    monkey_dict[monkey_dict[monkey_num]['false_con']]['items'].append(new)
            counter = len(monkey_dict[monkey_num]['items'])
            monkey_dict[monkey_num]['counter'] += counter
            del monkey_dict[monkey_num]['items'][:]

counter_list = []
for monkey in monkey_dict.keys():
    counter_list.append(monkey_dict[monkey]['counter'])
monkey_business = sorted(counter_list)[-1] * sorted(counter_list)[-2]

print(f'The answer to Part 2 is {monkey_business}')