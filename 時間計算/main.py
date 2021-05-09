import sys
import datetime


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[1::]:
    dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(days=int(line))
    print(dt.strftime('%Y-%m-%d'))
