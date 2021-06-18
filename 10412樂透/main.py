import sys


data = sys.stdin.read().splitlines()[1::]
prize_set = set([int(row) for row in data[0].split(',')])


for line in data[1::]:
    total = [0, 0, 0, 0]
    line = [int(row) for row in line.split(',')]
    for i in range(6):
        lotto_list = line.copy()
        lotto_list.pop(i)
        count = len(prize_set & set(lotto_list))
        if count > 1:
            total[count-2] += 1
    print(','.join([str(t) for t in total]))
