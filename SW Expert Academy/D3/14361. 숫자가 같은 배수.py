T = int(input())

for t in range(T):
    N = int(input())
    
    trigger = 'impossible'

    numbers = sorted(list(map(int, list(str(N)))))
    
    if len(str(N)) > 1:
        for i in range(2, 10):
            if sorted(list(map(int, list(str(N * i))))) == numbers:
                trigger = 'possible'
                break
    
    print(f'#{t+1} {trigger}')
        