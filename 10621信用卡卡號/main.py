import sys


for line in sys.stdin.read().splitlines()[1::]:
    line = list(line)
    line.reverse()
    total = 0
    for index, num in enumerate(line):
        if (index + 1) % 2 == 0:
            num = int(num) * 2
            if num >= 10:
                num = num - 9

        total += int(num)

    if total % 10 == 0:
        print('T')
    else:
        print('F')
