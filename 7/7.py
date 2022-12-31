import re

# Part 1
with open(r'./input') as f:
    terminal_lines = f.read().splitlines()

file_dictionary = {}
dirs_list = []

def set_nested(dictionary, existing_keys, key_to_set, value) -> None:
    for key in existing_keys:
        dictionary = dictionary.setdefault(key, {})
    dictionary[key_to_set] = value
    return

for line in terminal_lines:
    if dir_re := re.match(r'\$ cd (.*)', line):
        dirs = dir_re.group(1)
        if dirs == '..':
            dirs_list.pop()
        else:
            dirs_list.append(dirs)
    elif sub_dir_re := re.match(r'dir (.*)', line):
        sub_dir = sub_dir_re.group(1)
        set_nested(file_dictionary, dirs_list, sub_dir, dict())
    elif size_re := re.match(r'(\d+) (.*)', line):
        size = int(size_re.group(1))
        file = size_re.group(2)
        set_nested(file_dictionary, dirs_list, file, size)
    
def directory_size(dictionary):
    return sum([directory_size(value) if isinstance(value, dict) else value for value in dictionary.values()])

def traverse_dict(dictionary, sizes=None, directories=None):
    if not sizes:
        sizes = []
    if not directories:
        directories = []

    for key, value in dictionary.items():
        if not isinstance(value, dict):
            continue
        sizes.append(directory_size(value))
        directories.append(key)
        traverse_dict(value, sizes, directories)
    return directories, sizes

dirs_all, directory_sizes = traverse_dict(file_dictionary)

ans1 = sum([size_lim for size_lim in directory_sizes if size_lim <= 100000])
print(f'The answer to Part 1 is {ans1}')

# Part 2
total_size = 70000000
min_unused = 30000000
used = max(directory_sizes)
unused = total_size - used
target = min_unused - unused

ans2 = min([min_lim for min_lim in directory_sizes if min_lim >= target])
deleted_dir = dirs_all[directory_sizes.index(ans2)]
print(f'The answer to Part 2 is {ans2}. The deleted directory was {deleted_dir}')