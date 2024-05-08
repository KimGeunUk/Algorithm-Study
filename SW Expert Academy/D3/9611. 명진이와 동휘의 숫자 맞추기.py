T = int(input())

for t in range(T):
    N = int(input())
    
    numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    for _ in range(N):
        a, b, c, d, S = input().split()
        a, b, c, d = map(int, (a, b, c, d))
        
        if S == 'NO':
            numbers -= {a, b, c, d}
        else:
            numbers &= {a, b, c, d}
        
    print(f'#{t+1} {numbers.pop()}')