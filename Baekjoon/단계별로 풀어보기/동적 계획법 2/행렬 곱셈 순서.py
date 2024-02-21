import sys
input = sys.stdin.readline

N = int(input())

M = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * N
DP[0] = M[0][0] * M[0][1] # 5 * 3
DP[1] = DP[0] * M[1][1] # 5 * 3 * 2
DP[2] = min(DP[1] + M[0][0] * M[2][0] * M[2][1], M[1][0] * M[1][1] * M[2][1] + DP[0] * M[2][1])

if N > 3:
    for i in range(3, N):        
        DP[i] = min(DP[i-1] + M[i-2][0] * M[i][0] * M[i][1], M[i-1][0] * M[i-1][1] * M[i][1] + DP[i-2] * M[i][1])

print(DP[-1])