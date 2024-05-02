T = int(input())

for t in range(T):
    D, L, N = map(int, input().split())
    
    sum_ = D
    for n in range(N - 1):
        sum_ += D + D * ((n + 1) * (L / 100))
    
    print(f'#{t+1} {int(sum_)}')