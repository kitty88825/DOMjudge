import sys


for row in sys.stdin.read().splitlines()[1::]:
    data = [txt.split('.') for txt in row.split('/')]
    result = list()
    for d1, d2 in zip(data[0], data[1]):
        result.append(str(int(d1) | (255-int(d2))))

    print('.'.join(result))
