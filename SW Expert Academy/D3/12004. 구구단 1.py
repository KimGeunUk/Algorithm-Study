T = int(input())

for t in range(T):
    N = int(input())
    
    for i in range(1, 10):
        if N % i == 0 and 1 <= N // i <= 9:
            print(f'#{t+1} Yes')
            break
    else:
        print(f'#{t+1} No')