import sys


for line in sys.stdin.read().splitlines()[1::]:
    data = [int(i) for i in line.split(',')]
    y = int((data[3] - data[1] * data[0]) / (data[2] - data[1]))
    x = data[0] - y

    print(f'{x},{y}')
