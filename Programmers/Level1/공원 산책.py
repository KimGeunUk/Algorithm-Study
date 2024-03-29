def solution(park, routes):
    # E, W, N, S
    direct = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    
    x, y = 0, 0 # 열 행
    n, m = len(park[0]), len(park) # 열 행
    
    maps = []
    for idx1, p in enumerate(park):
        map = []
        for idx2, p_ in enumerate(p):
            if p_ == 'S':
                x = idx2
                y = idx1
            map.append(p_)
        maps.append(map)
        map = []
    
    for route in routes:
        d, num = route.split(' ')
        
        px, py = x, y
        for _ in range(int(num)):
            nx, ny = x + direct[d][1], y + direct[d][0]
            if (nx >= n or nx < 0) or (ny >= m or ny < 0) or (maps[ny][nx] == 'X'):
                x, y = px, py
                break
            else:
                x, y = nx, ny

    return [y, x]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]	)) # [2,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]	)) # [0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"] )) # [0,0]

print(solution(["OSO","OOO","OOO","OOO"], ["W 2"])) # [0,1]