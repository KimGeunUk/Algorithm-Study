def solution(m, n, puddles):
    answer = 0
    # m = 열, n = 행
    maps = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        maps[puddle[1]-1][puddle[0]-1] = -1
    
    # 오른쪽과 아래쪽으로만 움직여
    dx = [1, 0]
    dy = [0, 1]
    
    x, y = 0, 0
    
    def dfs(x, y):
        if x == m-1 and y == n-1:
            maps[n-1][m-1] = maps[n-1][m-1] + 1
            return maps

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ny < n and nx < m:                
                if maps[ny][nx] != -1:
                    dfs(nx, ny)
                    
        return maps
    
    dfs(x, y)
    answer = maps[-1][-1]

    return answer % 1000000007

def solution(m, n, puddles):    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    puddles = [[y, x] for [x, y] in puddles]    
        
    dp[1][1] = 1
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp)
    return dp[-1][-1] % 1000000007

print(solution(4, 3, [[2, 2]])) # 4
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]])) # 0