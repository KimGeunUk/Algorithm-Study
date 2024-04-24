T = int(input())

for t in range(T):
    N = int(input())
    
    if N % 2 == 0: print(f'#{t+1} Alice')
    else: print(f'#{t+1} Bob')