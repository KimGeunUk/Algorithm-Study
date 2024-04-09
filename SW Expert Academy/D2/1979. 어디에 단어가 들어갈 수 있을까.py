T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    answer = 0

    for row in maps:
        _sum = 0
        for col in row:
            if col == 0:
                if _sum == K:
                    answer += 1
                _sum = 0
            else:
                _sum += 1
        
        if _sum == K:
            answer += 1
    
    maps = list(map(list, zip(*maps)))
    
    for row in maps:
        _sum = 0
        for col in row:
            if col == 0:
                if _sum == K:
                    answer += 1
                _sum = 0
            else:
                _sum += 1
        
        if _sum == K:
            answer += 1
            
    print(f'#{i} {answer}')