import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

n, m, h = map(int, input().split())

maps = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

ripenses = deque([[i, j, k] for i in range(h) for j in range(m) for k in range(n) if maps[i][j][k] == 1])

while ripenses:
    p = ripenses.popleft()
    
    for l in range(6):
        nz, ny, nx = p[0] + dz[l], p[1] + dy[l], p[2] + dx[l]
        
        if (-1 < nz < h) and (-1 < ny < m) and (-1 < nx < n) and maps[nz][ny][nx] == 0:
            maps[nz][ny][nx] = maps[p[0]][p[1]][p[2]] + 1  
            ripenses.append([nz, ny, nx])

count = 0

for i in range(h): # z
    for j in range(m): # y
        for k in range(n): # x
            if maps[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                count = max(count, maps[i][j][k])
    
print(count - 1)