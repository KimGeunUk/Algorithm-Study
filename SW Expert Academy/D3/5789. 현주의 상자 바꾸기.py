T = int(input())

for t in range(T):
    N, Q = map(int, input().split())
    li = [0 for _ in range(N)]
    
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            li[j-1] = i + 1
    
    print(f'#{t+1}', end=' ')
    print(' '.join(map(str, li)))