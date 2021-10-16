import sys
from datetime import datetime

ddd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for row in sys.stdin.read().splitlines()[1::]:
    line = row.split()
    data = f'2021-{line[0]}-{line[1]}'
    ans = datetime.strptime(data, "%Y-%m-%d")
    # print(ans.isoweekday())
    print(ddd[ans.isoweekday()-1])
