import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        if x == M-1 and y == N-1:
            return count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, count + 1))

result = bfs()
print(result)
