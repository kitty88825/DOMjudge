import sys


for line in sys.stdin.read().splitlines()[1::]:
    row = [i for i in line]
    s_lower = 0
    s_up = 0

    s_lower = row.count('s')
    s_up = row.count('S')
    print(f'{s_lower},{s_up}')
