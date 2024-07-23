import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

maps = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(r, c):
    cnt = 1  
    queue = deque([(r, c)])
    visited[r][c] = True
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if -1 < nx < N and -1 < ny < N and maps[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    
    return cnt


result = []

for r in range(N):
    for c in range(N):
        if maps[r][c] == 1 and visited[r][c] == False:
            result.append(bfs(r, c))
            
result.sort()

print(len(result))
for r in result:
    print(r)