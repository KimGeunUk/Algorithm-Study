T = int(input())

for i in range(T):
    N = int(input())
    
    numbers = [0, 0, 0, 0, 0]
    
    while True:
        d, m = divmod(N, 11)
        if m == 0:
            numbers[4] += 1
            N = d
        else:
            break
    
    while True:
        d, m = divmod(N, 7)
        if m == 0:
            numbers[3] += 1
            N = d
        else:
            break
    
    while True:
        d, m = divmod(N, 5)
        if m == 0:
            numbers[2] += 1
            N = d
        else:
            break
        
    while True:
        d, m = divmod(N, 3)
        if m == 0:
            numbers[1] += 1
            N = d
        else:
            break
        
    while True:
        d, m = divmod(N, 2)
        if m == 0:
            numbers[0] += 1
            N = d
        else:
            break
    
    print(f'#{i+1}', end=' ')
    print(' '.join(map(str, numbers)))