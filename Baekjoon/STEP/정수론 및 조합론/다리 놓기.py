def fac(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer 

T = int(input())

for _ in range(T):
    M, N = map(int, input().split())

    print((fac(N) // (fac(M) * fac(N-M))))