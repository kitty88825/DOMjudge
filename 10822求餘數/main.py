import sys


for line in sys.stdin.read().splitlines()[1::]:
    row = [int(i) for i in line.split()]
    print(row[0] ** row[1] % row[2])
