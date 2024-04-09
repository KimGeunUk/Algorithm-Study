T = int(input())

for i in range(1, T + 1):
    N = int(input())
    
    _sum = 0
    
    for j in range(1, N + 1):
        if j % 2 == 0:
            _sum -= j
        else:
            _sum += j
            
    print(f'#{i} {_sum}')