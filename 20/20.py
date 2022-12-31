with open(r'/home/macolella/AoC2022/20/input') as f:
    ordered_list = f.read().splitlines()

# Part 1
ordered_list = [(ind, int(num)) for ind, num in enumerate(ordered_list)]

def mix(ordered_list):
    N = len(ordered_list)
    for ind in range(N):
        prev_ind, num = ordered_list[ind]
        new_ind = (prev_ind + num - 1) % (N - 1) + 1
        ordered_list = [
            (other - (prev_ind < other <= new_ind) + (new_ind <= other < prev_ind), n)
            for other, n in ordered_list
        ]
        ordered_list[ind] = (new_ind, num)
    return ordered_list

mixed_list = mix(ordered_list)

zero_coord = [(i,j) for i, j in mixed_list if j == 0][0]
ind_one = ((1000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1
ind_two = ((2000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1
ind_three = ((3000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1

special_coords = [(i,j) for i, j in mixed_list if i == ind_one or i == ind_two or i == ind_three]

print(f'The answer to Part 1 is {sum([j for i, j in special_coords])}')

# Part 2
with open(r'/home/macolella/AoC2022/20/input') as f:
    ordered_list = f.read().splitlines()

decryption_key = 811589153
ordered_list = [(ind, int(num)*decryption_key) for ind, num in enumerate(ordered_list)]

def mix_ten(ordered_list):
    N = len(ordered_list)
    for _ in range(10):
        for ind in range(N):
            prev_ind, num = ordered_list[ind]
            new_ind = (prev_ind + num - 1) % (N - 1) + 1
            ordered_list = [
                (other - (prev_ind < other <= new_ind) + (new_ind <= other < prev_ind), n)
                for other, n in ordered_list
            ]
            ordered_list[ind] = (new_ind, num)
        print(f'mixed {_ + 1} times')
    return ordered_list

mixed_list = mix_ten(ordered_list)

zero_coord = [(i,j) for i, j in mixed_list if j == 0][0]
ind_one = ((1000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1
ind_two = ((2000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1
ind_three = ((3000 % len(mixed_list)) + (zero_coord[0] + 1)) % len(mixed_list) - 1

special_coords = [(i,j) for i, j in mixed_list if i == ind_one or i == ind_two or i == ind_three]

print(f'The answer to Part 2 is {sum([j for i, j in special_coords])}')