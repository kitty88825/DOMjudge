import sys


d = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', 'G': '16', 'H': '17', 'I': '34', 'J': '18', 'K': '19', 'L': '20', 'M': '21', 'N': '22', 'O': '35', 'P': '23', 'Q': '24', 'R': '25', 'S': '26', 'T': '27', 'U': '28', 'V': '29', 'W': '32', 'X': '30', 'Y': '31', 'Z': '33'}
qu = [8, 7, 6, 5, 4, 3, 2, 1, 1]


def check_uid(uid):
    if int(uid[1]) > 2:
        return 'F'

    total = 0
    english_byte = [int(i) for i in d[uid[0]]]
    total += english_byte[0] * 1 + english_byte[1] * 9
    for index, q in enumerate(qu):
        total += int(uid[index+1]) * q

    if total % 10 == 0:
        return 'T'
    else:
        return 'F'


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[1::]:
    i = [r for r in line]
    print(check_uid(i))
