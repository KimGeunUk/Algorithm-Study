import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins.sort()

DP = [0 for _ in range(k+1)]
DP[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        if j - coin >= 0:
            DP[j] = DP[j] + DP[j - coin]

print(DP[k])