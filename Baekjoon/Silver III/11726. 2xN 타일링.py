N = int(input())

DP = [1] * (N+1)
DP[1] = 1

for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[-1]%10007)