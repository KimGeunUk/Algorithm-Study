T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    A = input().split()
    B = input().split()
        
    Q = int(input())
    
    string = ''
    for j in range(Q):
        Y = int(input())        
        string += A[(Y % len(A)) - 1] + B[(Y % len(B)) - 1] + ' '
    print(f'#{i+1} {string}')