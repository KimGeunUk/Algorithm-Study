import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = -1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    count = 0
    
    def dfs(x, y):
        arr[y][x] = count
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if -1 < nx < M and -1 < ny < N and arr[ny][nx] == -1:
                dfs(nx, ny)

    
    for row in range(N):
        for col in range(M):
            if arr[row][col] == -1:
                count += 1
                dfs(col, row)
    
    print(count)