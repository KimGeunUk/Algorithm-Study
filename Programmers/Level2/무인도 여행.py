import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = []
    
    row, col = len(maps), len(maps[0])

    maps = [list(map) for map in maps]
    
    visit = [[False for _ in range(col)] for _ in range(row)]
    
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def dfs(x, y):
        visit[y][x] = True
        value = int(maps[y][x])
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx > -1 and nx < col) and (ny > -1 and ny < row):
                if maps[ny][nx] != 'X' and visit[ny][nx] == False:
                    value += dfs(nx, ny)
        
        return value

    for y, map in enumerate(maps):
        for x, m in enumerate(map):
            if m != 'X' and visit[y][x] == False:
                answer.append(dfs(x, y))

    if answer: return sorted(answer)
    else: return [-1]
        

print(solution(["X591X",
                "X1X5X",
                "X231X", 
                "1XXX1"])) # [1, 1, 27]

print(solution(["X59XX",
                "XXX5X",
                "X231X", 
                "1XXX1"])) # [1, 1, 27]

print(solution(["XXX",
                "XXX",
                "XXX"])) # [-1]