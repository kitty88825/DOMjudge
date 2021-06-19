import sys


for line in sys.stdin.read().splitlines()[1::]:
    data_list = line.split('/')
    result = [str(int(d1) & int(d2)) for d1, d2 in zip(data_list[0].split('.'), data_list[1].split('.'))]
    print('.'.join([r for r in result]))
