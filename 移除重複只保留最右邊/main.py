import sys


for line in sys.stdin.read().splitlines():
    result_list = []
    row = [i for i in line]
    row.reverse()
    for r in row:
        if r not in result_list:
            result_list.append(r)

    result_list.reverse()
    print(''.join(result_list))
