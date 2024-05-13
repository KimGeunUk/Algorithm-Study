T = int(input())

for t in range(T):
    N = int(input())
    
    A, B = [], []
    for _ in range(N):       
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    P = int(input())    
    C = [int(input()) - 1 for _ in range(P)]    
    D = [0 for _ in range(5001)]

    for a, b in zip(A, B):
        for i in range(a-1, b):
            D[i] += 1

    print(f'#{t+1}', end=' ')
    for c in C:
        print(D[c], end=' ')
    print()