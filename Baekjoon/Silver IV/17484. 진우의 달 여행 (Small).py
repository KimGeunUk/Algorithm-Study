n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
DP = [[[float('inf')] * m for _ in range(n)] for _ in range(3)]

for i in range(3):
    for j in range(m):
        DP[i][0][j] = arr[0][j]

for i in range(1, n):
    for j in range(m):
        if j > 0:
            DP[0][i][j] = min(DP[1][i-1][j-1], DP[2][i-1][j-1]) + arr[i][j]
            
        DP[1][i][j] = min(DP[0][i-1][j], DP[2][i-1][j]) + arr[i][j]
        
        if j < m-1:
            DP[2][i][j] = min(DP[1][i-1][j+1], DP[0][i-1][j+1]) + arr[i][j]

min_cost = float('inf')
for j in range(m):
    min_cost = min(min_cost, DP[0][-1][j], DP[1][-1][j], DP[2][-1][j])
print(min_cost)

"""
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

costs = []

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y, direct, cost):
    if y == n - 1:
        costs.append(cost)
        return

    for i in range(3):
        if i == direct: continue
        
        nx, ny = x + dx[i], y + dy[i]
        
        if (-1 < nx < m) and (-1 < ny < n):
            dfs(nx, ny, i, cost + arr[ny][nx])

for i in range(m):
    dfs(i, 0, -1, arr[0][i])

print(min(costs))
"""