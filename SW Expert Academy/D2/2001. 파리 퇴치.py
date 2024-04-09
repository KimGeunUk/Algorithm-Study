T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    arrays = [list(map(int, input().split())) for _ in range(N)]
   
    _max = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            array = arrays[i:i+M]
            
            _sum = 0
            for arr in array:
                _sum += sum(arr[j:j+M])
                
            _max = max(_max, _sum)
    
    print(f'#{t} {_max}')
        