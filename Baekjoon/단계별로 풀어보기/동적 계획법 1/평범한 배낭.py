import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수, 버틸 수 있는 무게
L = [list(map(int, input().split())) for _ in range(N)]
L = [[0, 0]] + L

DP = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W = L[i][0]
        V = L[i][1]
        
        if j < W:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(V + DP[i-1][j-W], DP[i-1][j])

print(DP[-1][-1])

#       0  1  2  3  4  5  6  7
#       0  0  0  0  0  0  0  0
# 6 13  0  0  0  0  0  0 13 13
# 4  8  0  0  0  0  8  8 13 13    
# 3  6  0  0  0  6  8  8 13 14
# 5 12  0  0  0  6  8 12 13 14
