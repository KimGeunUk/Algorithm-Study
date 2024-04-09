T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    
    numbers.sort()
    
    print(f'#{i} {int(round(sum(numbers[1:-1]) / len(numbers[1:-1]), 0))}')