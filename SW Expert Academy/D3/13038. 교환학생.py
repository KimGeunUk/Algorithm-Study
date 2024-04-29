T = int(input())

for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    min_ = float('inf')
    
    for _ in range(7):
        n = N
        count = 0
        while n > 0:
            for num in numbers:
                n -= num
                count += 1
                if n < 1: break

        numbers = numbers[1:] + [numbers[0]]
        min_ = min(min_, count)

    print(f'#{t+1} {min_}')