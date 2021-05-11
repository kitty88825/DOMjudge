import sys

from datetime import datetime


data = sys.stdin.read().splitlines()[1::]

for d1, d2 in zip(data[::2], data[1::2]):

    d1 = datetime.strptime(d1, '%d/%m/%Y')
    d2 = datetime.strptime(d2, '%d/%m/%Y')

    if d1.replace(year=d2.year) >= d2:
        print(d1.year - d2.year)
    else:
        print(d1.year - d2.year - 1)
