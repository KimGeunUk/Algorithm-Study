T = int(input())

for t in range(T):
    N = int(input())
    P = list(map(int, input().split()))
            
    count = 0
    
    for i in range(1, len(P)-1):
        L = [P[i-1], P[i], P[i+1]]
        min_, max_ = min(L), max(L)
        
        if min_ != P[i] and max_ != P[i]:
            count += 1
            
    print(f'#{t+1} {count}')