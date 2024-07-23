import sys
input = sys.stdin.readline

n, k = map(int, input().split())

values = list(set([int(input()) for _ in range(n)]))
values.sort()

DP = [float('inf')] * (k+1)
DP[0] = 0

for value in values:
    for i in range(value, k+1):
        DP[i] = min(DP[i], DP[i-value] + 1)

if DP[k] == float('inf'):
    print(-1)
else:
    print(DP[k])
        