import sys


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[1::]:
    data = [int(i) for i in line.split(',')]
    if data[0] % 2 == 0 or data[1] % 2 == 0:
        print('N')
    elif data[0] == 3 or data[1] == 3 or data[0] % 3 == 0 or data[1] % 3 == 0:
        print('N')
    else:
        if abs(data[0] - data[1]) == 2:
            print('Y')
        else:
            print('N')
