import sys


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[2::2]:
    row = [int(r) for r in line.split()]
    row.sort(reverse=True)
    money_list = row[2::3]
    total = 0
    if money_list:
        for m in money_list:
            total += m

    print(total)
