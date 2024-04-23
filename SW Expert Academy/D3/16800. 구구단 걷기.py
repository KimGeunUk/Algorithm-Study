T = int(input())

for i in range(T):
    N = int(input())
    
    for a in range(int(N**0.5) + 1, 0, -1):
        if N % a == 0:
            b = N // a
            
            print(f'#{i+1} {(b - 1) + (a - 1)}')
            break