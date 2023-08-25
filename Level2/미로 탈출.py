from collections import deque
def solution(maps):
    def bfs(sx, sy, tx, ty): 
        visit = [[0 for _ in range(col)] for _ in range(row)]
        
        Q = deque([(sx, sy)])
        
        visit[sy][sx] = 1
        
        while Q:
            x, y = Q.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (nx > -1 and nx < col) and (ny > -1 and ny < row):
                    if maps[ny][nx] != 'X' and visit[ny][nx] == False:
                        visit[ny][nx] = visit[y][x] + 1
                        Q.append((nx, ny))

        return visit[ty][tx] - 1

    
    for col, map in enumerate(maps):
        maps[col] = list(map)
        for row, m in enumerate(map):
            if m == 'S':
                sx, sy = row, col
            if m == 'E':
                ex, ey = row, col
            if m == 'L':
                lx, ly = row, col

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # maps 크기
    row, col = len(maps), len(maps[0])
         
    l_time = bfs(sx, sy, lx, ly)
    if l_time == -1: return -1
    
    e_time = bfs(lx, ly, ex, ey)
    if e_time == -1: return -1
    
    return l_time + e_time

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1
# print(solution(["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"])) # 8