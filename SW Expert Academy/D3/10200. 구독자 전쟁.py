T = int(input())

for t in range(T):
    N, A, B = map(int, input().split())
    
    print(f'#{t+1} ', end='')
    print(min(A, B), end=' ')
    
    if N <= A + B:
        print((A+B)-N)
    else:
        print(0)