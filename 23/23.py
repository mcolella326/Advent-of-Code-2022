with open(r'/home/macolella/AoC2022/23/input') as f:
    elf_positions = f.read().splitlines()

# Part 1
elves = set()
for ind_row, row in enumerate(elf_positions):
    for ind_col, char in enumerate(row):
        if char == '#':
            elves.add((ind_row, ind_col))

# Define Conway's-like diffusion function
def diffuse(limit):
    norths = [(-1, 0), (-1, 1), (-1, -1)]
    souths = [(1, 0), (1, 1), (1, -1)]
    wests = [(0, -1), (-1, -1), (1, -1)]
    easts = [(0, 1), (-1, 1), (1, 1)]
    dirs = [norths, souths, wests, easts]
    surrounding_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    diffuse_counter = 0
    dir_counter = 0
    potential_new_locs = []
    elf_dict = {elf: (0, 0) for elf in elves}

    # Define circular range function
    def crange(start, end, modulo):
        for i in range(start,end):
            yield i % modulo

    # Define proposal direction function
    def dirs_propose(elf):
        surrounding_pos = set()
        for dir in surrounding_dirs:
            surrounding_pos.add((elf[0] + dir[0], elf[1] + dir[1]))
        if surrounding_pos & set(elf_dict.keys()):
            for dir_ind in crange(dir_counter, dir_counter + len(dirs), len(dirs)):
                potential_pos = set()
                for dir in dirs[dir_ind]:
                    potential_pos.add((elf[0] + dir[0], elf[1] + dir[1]))
                if not potential_pos & set(elf_dict.keys()):
                    potential_new_locs.append((elf[0] + dirs[dir_ind][0][0], elf[1] + dirs[dir_ind][0][1]))
                    elf_dict[elf] = potential_new_locs[-1]
                    return
        potential_new_locs.append((elf))
        elf_dict[elf] = potential_new_locs[-1]
        return

    while diffuse_counter < limit:
        dir_counter %= len(dirs)
        for elf in elf_dict:
            dirs_propose(elf)

        for elf, new_loc in elf_dict.items():
            if potential_new_locs.count(new_loc) > 1:
                elf_dict[elf] = elf
        elf_dict = {new_loc: old_loc for old_loc, new_loc in elf_dict.items()}
        potential_new_locs = []
        diffuse_counter += 1
        dir_counter += 1

    return set(elf_dict.keys())

diffused_elves = diffuse(10)

min_row = min(diffused_elves, key=lambda x: x[0])[0]
max_row = max(diffused_elves, key=lambda x: x[0])[0]
min_col = min(diffused_elves, key=lambda x: x[1])[1]
max_col = max(diffused_elves, key=lambda x: x[1])[1]

space = {(row, col) for col in range(min_col, max_col + 1) for row in range(min_row, max_row + 1)}
print(f'The answer to Part 1 is {len(space - diffused_elves)}')

# Part 2
# Define Conway's-like diffusion function
def diffuse_stable():
    norths = [(-1, 0), (-1, 1), (-1, -1)]
    souths = [(1, 0), (1, 1), (1, -1)]
    wests = [(0, -1), (-1, -1), (1, -1)]
    easts = [(0, 1), (-1, 1), (1, 1)]
    dirs = [norths, souths, wests, easts]
    surrounding_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    diffuse_counter = 0
    dir_counter = 0
    potential_new_locs = []
    elf_dict = {elf: (0, 0) for elf in elves}

    # Define circular range function
    def crange(start, end, modulo):
        for i in range(start,end):
            yield i % modulo

    # Define proposal direction function
    def dirs_propose(elf):
        surrounding_pos = set()
        for dir in surrounding_dirs:
            surrounding_pos.add((elf[0] + dir[0], elf[1] + dir[1]))
        if surrounding_pos & set(elf_dict.keys()):
            for dir_ind in crange(dir_counter, dir_counter + len(dirs), len(dirs)):
                potential_pos = set()
                for dir in dirs[dir_ind]:
                    potential_pos.add((elf[0] + dir[0], elf[1] + dir[1]))
                if not potential_pos & set(elf_dict.keys()):
                    potential_new_locs.append((elf[0] + dirs[dir_ind][0][0], elf[1] + dirs[dir_ind][0][1]))
                    elf_dict[elf] = potential_new_locs[-1]
                    return
        potential_new_locs.append((elf))
        elf_dict[elf] = potential_new_locs[-1]
        return

    while list(elf_dict.keys()) != list(elf_dict.values()):
        dir_counter %= len(dirs)
        for elf in elf_dict:
            dirs_propose(elf)

        for elf, new_loc in elf_dict.items():
            if potential_new_locs.count(new_loc) > 1:
                elf_dict[elf] = elf
        elf_dict = {new_loc: old_loc for old_loc, new_loc in elf_dict.items()}
        potential_new_locs = []
        diffuse_counter += 1
        dir_counter += 1

    return diffuse_counter

print(f'The answer to Part 2 is {diffuse_stable()}')