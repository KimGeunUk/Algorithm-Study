T = int(input())

for t in range(T):
    N = int(input())
    
    if N % 2 == 0:
        print(f'#{t+1} Even')
    else:
        print(f'#{t+1} Odd')