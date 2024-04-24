T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(T):
    n, m = map(int, input().split())
    
    arr = [list(input().strip()) for _ in range(n)]
    
    trigger = 'possible'
    
    for i in range(n):
        for j in range(m):
            if trigger:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    
                    if -1 < nx < n and -1 < ny < m:
                        if arr[i][j] == '#':
                            if arr[nx][ny] == '?' or arr[nx][ny] == '.':
                                arr[nx][ny] = '.'
                            else:
                                trigger = 'impossible'
                        elif arr[i][j] == '.':
                            if arr[nx][ny] == '?' or arr[nx][ny] == '#':
                                arr[nx][ny] = '#'
                            else:
                                trigger = 'impossible'
                                
    print(f'#{t+1} {trigger}')