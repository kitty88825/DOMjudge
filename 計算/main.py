import sys


def count(n, k):
    if n == 0:
        return 0

    if k == 0:
        return 1

    dp = [['' for i in range(12)] for j in range(98)]
    # print(dp)
    if dp[n][k] != -1:
        return dp[n][k]

    val = 0
    i = 0
    while i < n and k-i >= 0:
        i += 1
        val += count(n-1, k-i)

    dp[n][k] = val
    return dp[n][k]


# 第一筆為 input 數量
for line in sys.stdin.read().splitlines()[1::]:
    n, k = line.split(' ')
    print(count(int(n), int(k)))
