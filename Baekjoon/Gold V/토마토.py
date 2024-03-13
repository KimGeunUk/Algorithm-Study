import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maps = [list(map(int, input().split())) for _ in range(m)]
visited = []
count = 0

while True:
    check = False
    ripenses = []
    
    for i in range(m): # y
        for j in range(n): # x            
            if maps[i][j] == -1: continue
            elif maps[i][j] == 1:
                if [i, j] not in visited:
                    ripenses.append([i, j])
                    visited.append([i, j])
    
    for ripen in ripenses:
        for k in range(4):
            nx, ny = ripen[1] + dy[k], ripen[0] + dx[k]
            
            if (-1 < ny < m) and (-1 < nx < n) and maps[ny][nx] == 0:
                maps[ny][nx] = 1                        
                check = True
                        
    if check == False:
        for i in range(m): # y
            for j in range(n): # x            
                if maps[i][j] == 0:
                    count = 0
        break
    
    count += 1            

print(count)