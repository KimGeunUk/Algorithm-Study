def dfs(N, M, LIST, start):    
    if len(LIST) == M:
        print(*LIST)

    for i in range(start, N+1):
        if i not in LIST:
            LIST.append(i)
            dfs(N, M, LIST, i+1)
            LIST.pop()

N, M = map(int, input().split())
dfs(N, M, [], 1)

def dfs(N, M, LIST):    
    if len(LIST) == M:
        print(*LIST)

    for i in range(1, N+1):
        if i not in LIST:
            if len(LIST) > 0 and max(LIST) > i:
                continue
            else:
                LIST.append(i)
                dfs(N, M, LIST)
                LIST.pop()

N, M = map(int, input().split())
dfs(N, M, [])

from itertools import combinations as cb

N, M = map(int, input().split())

for i in sorted(list(cb(range(1, N+1), M))):
    print(*i)