N = int(input())

R, G, B = map(int, input().split())

DP = [[0] * 3 for _ in range(N+1)]

DP[1][0] = R
DP[1][1] = G
DP[1][2] = B

for i in range(2, N+1):
    R, G, B = map(int, input().split())
    
    DP[i][0] += R + min(DP[i-1][1], DP[i-1][2])
    DP[i][1] += G + min(DP[i-1][0], DP[i-1][2])
    DP[i][2] += B + min(DP[i-1][0], DP[i-1][1])

print(min(DP[-1]))