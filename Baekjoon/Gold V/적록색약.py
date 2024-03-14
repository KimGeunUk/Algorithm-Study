import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

maps = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(sx, sy, color):
    visited[sy][sx] = True

    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        
        if (-1 < ny < n) and (-1 < nx < n) and maps[ny][nx] == color and visited[ny][nx] == False:
            dfs(nx, ny, color)

answer = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n): # y
    for j in range(n): # x
        if maps[i][j] == 'R' and visited[i][j] == False:
            dfs(j, i, 'R')
            answer += 1
        elif maps[i][j] == 'G' and visited[i][j] == False:
            dfs(j, i, 'G')
            answer += 1
        elif maps[i][j] == 'B' and visited[i][j] == False:
            dfs(j, i, 'B')
            answer += 1

print(answer, end=' ')

# convert G -> R
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'G':
            maps[i][j] = 'R'

answer = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n): # y
    for j in range(n): # x
        if maps[i][j] == 'R' and visited[i][j] == False:
            dfs(j, i, 'R')
            answer += 1
        elif maps[i][j] == 'B' and visited[i][j] == False:
            dfs(j, i, 'B')
            answer += 1

print(answer)
