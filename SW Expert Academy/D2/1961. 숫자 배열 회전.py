T = int(input())

for i in range(T):
    N = int(input())
    
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    rotate90 = [[0 for _ in range(N)] for _ in range(N)]
    rotate180 = [[0 for _ in range(N)] for _ in range(N)]
    rotate270 = [[0 for _ in range(N)] for _ in range(N)]
    
    for r, row in enumerate(maps):
        for c, col in enumerate(row):
            nr, nc = c, N - 1 - r
            rotate90[nr][nc] = maps[r][c]
            
            nr, nc = N - 1 - r, N - 1 - c
            rotate180[nr][nc] = maps[r][c]
            
            nr, nc = N - 1 - c, r
            rotate270[nr][nc] = maps[r][c]

    print(f'#{i+1}')
    for r90, r180, r270 in zip(rotate90, rotate180, rotate270):
        print(''.join(map(str, r90)), end=' ')
        print(''.join(map(str, r180)), end=' ')
        print(''.join(map(str, r270)))