import sys


for line in sys.stdin.read().splitlines():
    total = 0
    total_list = []

    for index, value in enumerate(line):
        if index + 1 != len(line):
            total += 1
            if value > line[index + 1]:
                total_list.append(total)
                total = 0
        else:
            total += 1

    total_list.append(total)
    print(max(total_list))

# 下方程式會出現 wrong-answer 原因為使用 set 並未計算到第二次出現的字串
# for line in sys.stdin.read().splitlines():
#     row = list(set(line))
#     row.sort(key=line.index)
#     total_list = []
#     total = 0

#     for index, value in enumerate(row):
#         total += line.count(value)
#         if index + 1 != len(row) and value > row[index + 1]:
#             total_list.append(total)
#             total = 0

#     total_list.append(total)
#     print(max(total_list))
