T = int(input())

for i in range(T):
    N = int(input())
    
    count = 0
    
    for x in range(N + 1):
        for y in range(N + 1):
            if x ** 2 + y ** 2 <= N ** 2:
                if x == 0 or y == 0:
                    count += 2
                else:
                    count += 4
                
    print(f'#{i+1} {count - 1}')