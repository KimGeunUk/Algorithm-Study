T = int(input())

for t in range(T):
    p, q = map(float, input().split())
    
    A = (1-p) * q
    B = p * (1-q) * q
    
    if A < B: print(f'#{t+1} YES')
    else: print(f'#{t+1} NO')