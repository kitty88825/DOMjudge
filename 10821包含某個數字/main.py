import sys


for line in sys.stdin.read().splitlines()[1::]:
    result = []
    row = [int(i) for i in line.split()]
    for i in range(row[0], row[1] + 1):
        if len(str(i).split(str(row[2]))) > 1:
            result.append(i)

    print(len(result))
