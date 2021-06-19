import sys


for line in sys.stdin.read().splitlines()[1::]:
    print(len(line.split()))
