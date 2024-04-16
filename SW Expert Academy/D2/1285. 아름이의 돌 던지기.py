T = int(input())

for i in range(T):
    N = int(input())
    
    stones = list(map(int, input().split()))
    
    count = 0
    min_ = float('inf')
    
    for stone in stones:
        if min_ > abs(stone):
            min_ = abs(stone)
            count = 1
        elif min_ == abs(stone):
            count += 1
    
    print(f'#{i+1} {min_} {count}')