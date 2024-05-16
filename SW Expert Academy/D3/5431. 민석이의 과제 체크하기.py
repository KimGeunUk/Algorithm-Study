T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    
    L = {i for i in range(1, N+1)}
    
    array = list(map(int, input().split()))
    
    for a in array:
        L.remove(a)
    
    print(f'#{t+1}', end=' ')
    print(' '.join(map(str, sorted(list(L)))))