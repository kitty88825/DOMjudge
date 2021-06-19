import sys


for line in sys.stdin.read().splitlines()[1::]:
    data = bin(int(line)).split('0b')[1]
    print(data.count('1'))
