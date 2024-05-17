limit = 10**6
prime = [True for _ in range(limit + 1)]
for i in range(2, limit + 1):
    if prime[i]:
        for j in range(i*i, limit + 1, i):
            prime[j] = False
prime[0], prime[1] = False, False

T = int(input())
for t in range(T):
    D, A, B = map(int, input().split())
    answer = 0
    
    for i in range(A, B+1):
        if prime[i] and str(D) in str(i):
            answer += 1
    
    print(f'#{t+1} {answer}')