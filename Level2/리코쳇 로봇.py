def solution(board):
    answer = 0
    
    visited = []
    row, col = len(board), len(board[0])
    for i in range(row):
        visited.append([0 for _ in range(col)])
        for j in range(col):            
            if board[i][j]=='R':
                rx, ry = i, j
            if board[i][j]=='G':
                gx, gy = i, j
    print(rx, ry, gx, gy)
    
    # U D L R
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while True:
        mv = []
        mv.append((rx, ry, 0))
        
        visited[rx][ry] = 1
        for v in visited:
            print(v)
        
        while len(mv) != 0:
            # 움직이기 전 위치 저장
            px, py, count = mv.pop(0)
            
            if (px, py) == (gx, gy):
                visited[rx][ry] = 1
                for v in visited:
                    print(v)
                return count
               
            for i in range(4):
                # 각 방향에 따라 움직인 후 위치 변수 생성
                nx, ny = px, py
                                         
                # 방향의 끝까지 이동
                while True:                    
                    if i == 0: # U
                        if nx+dx[i] >= 0 and board[nx+dx[i]][ny] != 'D':
                            nx, ny = nx+dx[i], ny+dy[i]
                        else:
                            break
                    elif i == 1: # D
                        if nx+dx[i] < row and board[nx+dx[i]][ny] != 'D':
                            nx, ny = nx+dx[i], ny+dy[i]
                        else:
                            break
                    elif i == 2: # L
                        if ny+dy[i] >= 0 and board[nx][ny+dy[i]] != 'D':
                            nx, ny = nx+dx[i], ny+dy[i]
                        else:
                            break
                    elif i == 3: # R
                        if ny+dy[i] < col and board[nx][ny+dy[i]] != 'D':
                            nx, ny = nx+dx[i], ny+dy[i]
                        else:
                            break
                    
                if visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    mv.append((nx, ny, count + 1))
                    
            answer += 1

        return -1



print(solution(["...D..R", 
                ".D.G...", 
                "....D.D", 
                "D....D.", 
                "..D...."])) # 7

# print(solution([".D.R", 
#                 "....", 
#                 ".G..", 
#                 "...D"])) # -1