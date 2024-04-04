T = int(input())

for i in range(1, T + 1):
    numbers = map(int, input().split())
    
    _sum = sum(numbers)
    
    print(f'#{i} {round(_sum / 10)}')