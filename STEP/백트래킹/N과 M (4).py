def dfs(N, M, LIST, start):    
    if len(LIST) == M:
        print(*LIST)
        return

    for i in range(start, N+1):
        LIST.append(i)
        dfs(N, M, LIST, i)
        LIST.pop()
        
N, M = map(int, input().split())
dfs(N, M, [], 1)