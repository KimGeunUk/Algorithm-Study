T = int(input())

for t in range(T):
    N = int(input())
    
    arr = [list(input().strip()) for _ in range(N)]
    flag = False

    for r, row in enumerate(arr):
        for c, col in enumerate(row):
            if flag: continue
            
            if col == "o":
                if c + 4 <= N - 1:
                    for i in range(c, c + 5):
                        if arr[r][i] != 'o': break
                    else: flag = True

                if r + 4 <= N - 1:
                    for i in range(r, r + 5):
                        if arr[i][c] != 'o': break
                    else: flag = True
                        
                if c - 4 >= 0 and r + 4 <= N - 1:
                    for i, j in zip(range(r, r + 5), range(c, c - 5, -1)):
                        if arr[i][j] != 'o': break
                    else: flag = True

                if c + 4 <= N - 1 and r + 4 <= N - 1:
                    for i, j in zip(range(r, r + 5), range(c, c + 5)):
                        if arr[i][j] != 'o': break
                    else: flag = True
    
    if flag: print(f'#{t+1} YES')
    else: print(f'#{t+1} NO')