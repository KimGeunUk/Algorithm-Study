T = int(input())

for i in range(1, T + 1):
    N = int(input())
    
    money = []
    
    d, m = divmod(N, 50000)    
    money.append(d)
    
    d, m = divmod(m, 10000)    
    money.append(d)
    
    d, m = divmod(m, 5000)    
    money.append(d)
    
    d, m = divmod(m, 1000)    
    money.append(d)
    
    d, m = divmod(m, 500)    
    money.append(d)
    
    d, m = divmod(m, 100)    
    money.append(d)
    
    d, m = divmod(m, 50)    
    money.append(d)
    
    d, m = divmod(m, 10)    
    money.append(d)

    print(f'#{i}')
    print(' '.join(map(str, money)))