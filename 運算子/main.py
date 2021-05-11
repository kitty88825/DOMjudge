import sys


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[1::]:
    row = [int(r) for r in line.split()]
    if row[0] < row[1]:
        print('<')
    elif row[0] > row[1]:
        print('>')
    else:
        print('=')
