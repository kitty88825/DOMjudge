import sys


for line in sys.stdin.read().splitlines()[1::]:
    row = [int(i) for i in line.split()]
    row.sort(reverse=True)
    print(' '.join([str(r) for r in row[:2:]]))
