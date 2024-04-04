T = int(input())

for i in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    answer = 0
    
    _max = numbers[-1]
    for num in numbers[-2::-1]:
        if _max >= num:
            answer += _max - num
        else:
            _max = num
    
    print(f'#{i} {answer}')
        