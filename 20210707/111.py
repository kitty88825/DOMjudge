import sys


for line in sys.stdin.read().splitlines()[1::]:
    text = str(bin(int(line)))
    text = text.split('0b')[-1]
    print(text.count('1'))
