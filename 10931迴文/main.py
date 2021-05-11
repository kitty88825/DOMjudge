import sys


def chech_result(num):
    return bool(num == num[::-1]), num[::-1]


for line in sys.stdin.read().splitlines()[1::]:
    start = line
    status, result = chech_result(start)
    while not status:
        start = str(int(start) + int(result))
        status, result = chech_result(start)

    print(result)
