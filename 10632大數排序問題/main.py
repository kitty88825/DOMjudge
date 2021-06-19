import sys


for line in sys.stdin.read().splitlines()[1::]:
    data = [int(i) for i in line.split(',')]
    data_c = data.copy()
    data_c.sort()

    result = list()
    for value in data:
        result.append(str(data_c.index(value) + 1))

    print(', '.join(result))
