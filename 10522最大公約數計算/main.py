import sys

from itertools import combinations


def gcd(x, y):
    max_num, min_num = max(x, y), min(x, y)
    if max_num % min_num == 0:
        return min_num
    else:
        return gcd(min_num, max_num % min_num)


for line in sys.stdin.read().splitlines()[1::]:
    line = line.split(',')
    result = list()
    for x, y in combinations(line, 2):
        result.append(gcd(int(x), int(y)))

    print(max(result))
