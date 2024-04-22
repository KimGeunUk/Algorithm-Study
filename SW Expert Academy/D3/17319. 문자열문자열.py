T = int(input())

for i in range(T):
    N = int(input())
    S = input().strip()
    
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]: print(f'#{i+1} Yes')
        else: print(f'#{i+1} No')
    else:
        print(f'#{i+1} No')