T = int(input())

for i in range(1, T + 1):
    numbers = map(int, input().split())
    
    _sum = 0
    for number in numbers:
        if number % 2 == 1:
            _sum += number
    print(f'#{i} {_sum}')