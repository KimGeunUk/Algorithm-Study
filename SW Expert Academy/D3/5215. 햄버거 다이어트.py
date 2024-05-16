from itertools import combinations

T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    max_ = -1
    for i in range(1, N+1):
        C = combinations(array, i)

        for com in C:     
            T, K = 0, 0
            
            for co in com:
                T += co[0]
                K += co[1]

            if K <= L:
                max_ = max(max_, T)
    
    print(f'#{t+1} {max_}')