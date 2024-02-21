T = int(input())

for i in range(T):    
    k = int(input())
    n = int(input())
    
    maps = [[i for i in range(1, n+1)] for _ in range(k+1)]
    
    for j in range(1, k+1):
        for i in range(1, n):
            maps[j][i] = maps[j-1][i] + maps[j][i-1]
        
    print(maps[k][n-1])
        