T = int(input())

for t in range(T):
    N = int(input())
    
    arr = [list(input().strip()) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    trigger = None
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#' and visited[r][c] == False and trigger == None:
                visited[r][c] = True
                count = 1
                
                nc = c
                while True:
                    nc = nc + 1
                    
                    if -1 < nc < N and arr[r][nc] == '#' and visited[r][nc] == False:
                        visited[r][nc] = True
                        count += 1
                    else:
                        break
                                   
                trigger = 'yes'
                for i in range(1, count):
                    for j in range(count):
                        if -1 < r + i < N and -1 < c + j < N and arr[r + i][c + j] == '#' and visited[r + i][c + j] == False:
                            visited[r + i][c + j] = True
                            continue
                        else:
                            trigger = 'no'
            
            elif arr[r][c] == '#' and visited[r][c] == False and trigger != None: trigger = 'no'
            elif trigger == 'no': break
    
    print(f'#{t+1} {trigger}')   