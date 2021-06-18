import sys


for line in sys.stdin.read().splitlines()[2::2]:
    total = 0
    row = iter(line.split(','))
    now_where = int(next(row))
    while True:
        try:
            next_where = int(next(row))
            if now_where < next_where:
                total += (next_where - now_where) * 20
            elif now_where > next_where:
                total += (now_where - next_where) * 10
            else:
                total += 0
            now_where = next_where
        except StopIteration:
            break
    print(total)
