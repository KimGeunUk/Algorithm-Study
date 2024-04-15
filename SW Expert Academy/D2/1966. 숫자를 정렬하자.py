T = int(input())

for i in range(T):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    
    print(f'#{i+1}', end=' ')
    print(' '.join(map(str, numbers)))
    
    