T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    maps = [[0 for _ in range(N)] for _ in range(N)]
    
    maps[N//2-1][N//2-1], maps[N//2][N//2] = 2, 2
    maps[N//2-1][N//2], maps[N//2][N//2-1] = 1, 1
    
    for _ in range(M):
        r, c, stone = map(int, input().split())
        r, c = r-1, c-1
        
        maps[r][c] = stone
        
        # 왼
        for i in range(2, c+1):
            if maps[r][c-i] == stone:
                for j in range(1, i):
                    maps[r][c-j] = stone
                break
            elif maps[r][c-i] == 0: break
        
        # 오
        for i in range(2, N-c):
            if maps[r][c+i] == stone:
                for j in range(1, i):
                    maps[r][c+j] = stone
                break
            elif maps[r][c+i] == 0: break
            
        # 상
        for i in range(2, r+1):
            if maps[r-i][c] == stone:
                for j in range(1, i):
                    maps[r-j][c] = stone
                break
            elif maps[r-i][c] == 0: break
        
        # 하
        for i in range(2, N-r):
            if maps[r+i][c] == stone:
                for j in range(1, i):
                    maps[r+j][c] = stone
                break
            elif maps[r+i][c] == 0: break
        
        # 왼상
        for i in range(1, min(r, c)+1):
            if maps[r-i][c-i] == stone:
                for j in range(1, i):
                    maps[r-j][c-j] = stone
                break
            elif maps[r-i][c-i] == 0: break
        
        # 우상
        for i in range(1, min(r+1, N-c)):
            if maps[r-i][c+i] == stone:
                for j in range(1, i):
                    maps[r-j][c+j] = stone
                break
            elif  maps[r-i][c+i] == 0: break
        
        # 왼하
        for i in range(1, min(N-r, c+1)):
            if maps[r+i][c-i] == stone:
                for j in range(1, i):
                    maps[r+j][c-j] = stone
                break
            elif maps[r+i][c-i] == 0: break
        
        # 우하
        for i in range(1, min(N-r, N-c)):
            if maps[r+i][c+i] == stone:
                for j in range(1, i):
                    maps[r+j][c+j] = stone
                break     
            elif maps[r+i][c+i] == 0: break

    
    black = 0
    white = 0
    for ma in maps:
        for m in ma:
            if m == 1: black += 1
            elif m == 2: white += 1
            
    print(f'#{t+1} {black} {white}')