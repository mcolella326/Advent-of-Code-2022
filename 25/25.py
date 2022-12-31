with open(r'/home/macolella/AoC2022/25/input') as f:
    fuels = f.read().splitlines()

snafu = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

def s2d(snafu_num):
    num_dec = 0
    for ind, num in enumerate(snafu_num[::-1]):
        num_dec += 5**ind * snafu[num]
    return num_dec

def d2s(num_dec):
    snafu_num = ''
    while num_dec > 0:
        base_five = num_dec % 5
        if base_five == 0:
            snafu_num = '0' + snafu_num
            num_dec = num_dec // 5
        elif base_five == 1:
            snafu_num = '1' + snafu_num
            num_dec -= 1
            num_dec = num_dec // 5
        elif base_five == 2:
            snafu_num = '2' + snafu_num
            num_dec -= 2
            num_dec = num_dec // 5
        elif base_five == 3:
            snafu_num = '=' + snafu_num
            num_dec += 2
            num_dec = num_dec // 5
        elif base_five == 4:
            snafu_num = '-' + snafu_num
            num_dec += 1
            num_dec = num_dec // 5
    return snafu_num

total_dec = 0
for snafu_num in fuels:
    total_dec += s2d(snafu_num)

snafu_ans = d2s(total_dec)
print(f'The answer to Part 1 is {snafu_ans}')