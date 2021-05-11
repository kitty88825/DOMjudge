import sys


data = [1, 10, 100, 1000, 10000]

for line in sys.stdin.read().splitlines()[1::]:
    row = [int(i) for i in line]
    row.reverse()
    a = 0
    b = 0
    for index, value in enumerate(row):
        if value == 4:
            b += data[index]

    a = int(line) - b
    print(a, b)
