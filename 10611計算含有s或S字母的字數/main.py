import sys


for line in sys.stdin.read().splitlines()[1::]:
    total = 0
    line = line.lower()
    for voca in line.split():
        if 's' in voca:
            total += 1

    print(total)
