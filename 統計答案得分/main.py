import sys


for line in sys.stdin.read().splitlines()[1::]:
    total = 0
    count = 0

    for j in [i for i in line]:
        if j == 'O':
            count += 1
        else:
            total += int((1 + count) * count / 2)
            count = 0

    total += int((1 + count) * count / 2)
    print(total)
