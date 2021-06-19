import sys

from itertools import permutations


for line in sys.stdin.read().splitlines()[1::]:
    line = line.split(',')
    key_index = int(line[1]) - 1
    check_index = int(line[2]) - 1

    data = list()
    for value in permutations(line[0], len(line[0])):
        data.append(int(''.join(value)))

    data.sort()
    key = list(str(data[key_index]))
    check = list(str(data[check_index]))
    a = 0
    for k, c in zip(key, check):
        if k == c:
            a += 1
    b = len(check) - a

    print(f'{a}A{b}B')
