import sys


def gcd(x, y):
    max_num, min_num = max(x, y), min(x, y)
    if max_num % min_num == 0:
        return min_num
    else:
        return gcd(min_num, max_num % min_num)


for line in sys.stdin.read().splitlines()[1::]:
    g = 0
    line = [int(i) for i in line.split(',')]
    for i in range(len(line)):
        if i == 0:
            g = line[i]
        else:
            g = gcd(g, line[i])

    print(g)
