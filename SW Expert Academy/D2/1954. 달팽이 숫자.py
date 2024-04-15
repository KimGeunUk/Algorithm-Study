T = int(input())

for i in range(T):
    N = int(input())
    
    maps = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    x, y, k = 0, 0, 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    maps[0][0] = 1
    
    for j in range(2, N**2 + 1):
        nx, ny = x + dx[k%4], y + dy[k%4]
        
        if -1 < nx < N and -1 < ny < N and maps[nx][ny] == 0:
            maps[nx][ny] = j
            x, y = nx, ny
        else:
            k += 1
            
            nx, ny = x + dx[k%4], y + dy[k%4]
            if -1 < nx < N and -1 < ny < N and maps[nx][ny] == 0:
                maps[nx][ny] = j
                x, y = nx, ny
    
    print(f'#{i+1}')
    for m in maps:
        print(' '.join(map(str, m)))
        