from collections import Counter

T = int(input())

for t in range(T):
    S = input().strip()
    H = int(input())
    L = list(map(int, input().split()))
    L = sorted(L)
    
    count = 0    
    for l in L:
        A = S[:l+count]
        B = S[l+count:]
        
        S = A + '-' + B
        count += 1
        
    print(f'#{t+1} {S}')