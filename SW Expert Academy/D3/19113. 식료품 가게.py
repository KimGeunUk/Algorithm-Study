T = int(input())

for i in range(T):
    N = int(input())
    
    prices = list(map(int, input().split()))
    answer = []
    
    while prices:
        price = prices.pop()        
        value = int(price * 0.75)
        if value in prices:
            prices.remove(value)
            answer.append(value)
        
    print(f'#{i+1}', end=' ')
    print(' '.join(map(str, sorted(answer))))