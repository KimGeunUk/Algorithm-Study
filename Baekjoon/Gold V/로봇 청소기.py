import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
        
    if maps[r][c] == 0:
        maps[r][c] = 2
        count += 1
    
    for i in range(4):
        d = (d - 1) % 4
        nr, nc = r + dx[d], c + dy[d]
        if (-1 < nr < n) and (-1 < nc < m) and (maps[nr][nc] == 0):
            r, c = nr, nc            
            break
    else:
        if maps[r - dx[d]][c - dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r - dx[d], c - dy[d]