# from itertools import permutations as per

# N, M = map(int, input().split())

# for i in sorted(list(per(range(1, N+1), M))):
#     print(*i)

def dfs(N, M, LIST):    
    if len(LIST) == M:
        print(*LIST)

    for i in range(1, N+1):
        if i not in LIST:
            LIST.append(i)
            dfs(N, M, LIST)
            LIST.pop()

N, M = map(int, input().split())
print(dfs(N, M, []))

