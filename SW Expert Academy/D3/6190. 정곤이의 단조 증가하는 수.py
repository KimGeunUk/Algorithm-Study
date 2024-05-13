from itertools import combinations

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort()
    
    C = combinations(A, 2)
    M = [a * b for (a, b) in C]
    M.sort(reverse=True)
    
    for m in M:
        strM = str(m)
        lenM = len(strM)
        trigger = True

        for k in range(lenM):
            for l in range(k+1, lenM):
                if not (int(strM[k]) <= int(strM[l])):
                    trigger = False
                    break
                
        if trigger: break
    
    if trigger: print(f'#{t+1} {m}')
    else: print(f'#{t+1} {-1}')
