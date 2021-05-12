import sys


data = sys.stdin.read().splitlines()[1::]

for s1, s2 in zip(data[::2], data[1::2]):
    s1 = s1.split(' ')[1::]
    s2 = s2.split(' ')[1::]
    count = 0

    for s in s1:
        if s2.count(s) >= 1:
            count += 1

    print(count)
