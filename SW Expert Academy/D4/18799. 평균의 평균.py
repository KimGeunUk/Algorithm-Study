from itertools import combinations

T = int(input())

for t in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    A = 0
    
    for i in range(1, N+1):
        C = combinations(S, i)
        for c in C:
            A += sum(c) / len(c)
    
    answer = A / (2**N - 1)
    if answer.is_integer():
        print(f'#{t+1} {int(answer)}')
    else:
        print(f'#{t+1} {answer:.20f}')