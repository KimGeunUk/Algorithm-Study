T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        N, M = M, N
        A, B = B, A
    
    max_ = -float('inf')
    
    for j in range(M - N + 1):
        sum_ = 0
        for a, b in zip(A, B[j:j+N]):
            sum_ += a * b

        max_ = max(max_, sum_)
    
    print(f'#{i+1} {max_}')