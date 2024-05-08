T = int(input())

for t in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L = sorted(L)
    
    trigger = False
    for i in range(len(L)-1, 0, -1):
        if trigger: break
        
        for j in range(i-1, -1, -1):
            if trigger: break
            
            m = L[i] * L[j]
            
            A = list(map(int, str(m)))
            B = [i for i in range(min(A), max(A)+1)]
            if A == B:
                print(f'#{t+1} {m}')
                trigger = True
                break
            
    if not trigger:
        print(f'#{t+1} -1')