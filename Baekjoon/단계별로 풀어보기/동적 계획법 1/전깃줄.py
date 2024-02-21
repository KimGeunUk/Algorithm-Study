N = int(input())

DP = [1] * N

lines = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[0])

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))