def dfs(N, M, LIST):    
    if len(LIST) == M:
        print(*LIST)
        return

    for i in range(1, N+1):
        LIST.append(i)
        dfs(N, M, LIST)
        LIST.pop()
        
N, M = map(int, input().split())
dfs(N, M, [])