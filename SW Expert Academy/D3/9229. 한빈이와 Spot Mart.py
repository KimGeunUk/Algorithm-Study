T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    trigger = False
    
    for i in range(N-1, 0, -1):
        if trigger: break
        
        L = A[i]
        for j in range(i-1, -1, -1):
            R = A[j]            
            if L + R <= M:
                trigger = True
                break
    
    if trigger:
        print(f'#{t+1} {L + R}')
    else:
        print(f'#{t+1} {-1}')