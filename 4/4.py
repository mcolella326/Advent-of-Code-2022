import re

#Part 1
with open(r'./input') as f:
    sections = f.read().splitlines()

# def make_set(section1, section2):
#     match1 = re.match(r'(\d*)-(\d*)', section1)
#     match2 = re.match(r'(\d*)-(\d*)', section2)
#     set1 = set(range(int(match1.group(1)), int(match1.group(2)) + 1))
#     set2 = set(range(int(match2.group(1)), int(match2.group(2)) + 1))
#     return set1, set2

# sections = [make_set(*re.split(',', section)) for section in sections]


def g(section: str):  # 1-2
    a, b = map(int, section.split("-"))
    return set(range(a, b + 1))


def f(section: str):  # 1-2,3-4
    first_section, second_section = section.split(",")
    return g(first_section), g(second_section)


sections = [f(section) for section in sections]

counter = 0
for section in sections:
    section_intersection = section[0] & section[1]
    if (section_intersection == section[0]) or (section_intersection == section[1]):
        counter += 1

print(f'The answer to Part 1 is {counter}')

#Part 2
counter = 0
for section in sections:
    section_intersection = section[0] & section[1]
    if section_intersection:
        counter += 1

print(f'The answer to Part 2 is {counter}')