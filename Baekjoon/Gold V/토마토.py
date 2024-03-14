import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(m)]

ripenses = deque([[i, j] for i in range(m) for j in range(n) if maps[i][j] == 1])

while ripenses:
    p = ripenses.popleft()
    
    for k in range(4):
        ny, nx = p[0] + dy[k], p[1] + dx[k]
        
        if (-1 < ny < m) and (-1 < nx < n) and maps[ny][nx] == 0:
            maps[ny][nx] = maps[p[0]][p[1]] + 1  
            ripenses.append([ny, nx])
            
count = 0

for i in range(m): # y
    for j in range(n): # x            
        if maps[i][j] == 0:
            print(-1)
            exit(0)
        else:
            count = max(count, maps[i][j])
    
print(count - 1)