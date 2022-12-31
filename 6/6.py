# Part 1
with open(r'./input') as f:
    code = f.read()

code = [letter for letter in code]

def duplicate_check(num):
    test_packet = code[:num]
    counter = num
    while len(test_packet) != len(set(test_packet)):
        del test_packet[0]
        test_packet.append(code[counter])
        counter += 1
    return counter

ans1 = duplicate_check(4)

print(f'The answer to Part 1 is {ans1}')

# Part 2
ans2 = duplicate_check(14)

print(f'The answer to Part 2 is {ans2}')