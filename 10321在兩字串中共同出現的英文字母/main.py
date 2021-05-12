import sys


data = sys.stdin.read().splitlines()[1::]

for s1, s2 in zip(data[::2], data[1::2]):
    result = []
    for s in s1:
        if s2.count(s) >= 1 and s not in result:
            result.append(s)

    if result:
        result.sort()
        print(''.join(result))
    else:
        print('N')
