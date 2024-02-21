N = int(input())

DP = [[0 for _ in range(i)] for i in range(1, N+1)]

DP[0][0] = int(input())

for i in range(1, N):
    nums = list(map(int, input().split()))
    for j in range(i+1):
        if j == 0:
            DP[i][0] = DP[i-1][0] + nums[0]
        elif j == i:
            DP[i][i] = DP[i-1][i-1] + nums[i]
        else:
            DP[i][j] = max(DP[i-1][j-1] + nums[j], DP[i-1][j] + nums[j])

print(max(DP[-1]))