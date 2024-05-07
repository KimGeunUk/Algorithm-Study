T = int(input())

for t in range(T):
    N = int(input())
    
    A = list(map(int, input().split()))
    B = set(A)
    
    if len(A) == len(B): print(f'#{t+1} Yes')
    else: print(f'#{t+1} No')