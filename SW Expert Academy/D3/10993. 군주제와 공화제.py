T = int(input())

for t in range(T):
    N = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    threats = []
    answer = [-1 for _ in range(N)]
    
    for i in range(N):
        temp = []
        for j in range(N):
            if i == j: continue
            
            x_i, y_i, s_i = arr[i]
            x_j, y_j, s_j = arr[j]
            
            # j -> i
            s = s_j / ((x_i - x_j)**2 + (y_i - y_j)**2)

            if s_i < s:
                temp.append([j, s])
        threats.append(temp)
    
    for i, threat in enumerate(threats):
        if threat == []: answer[i] = 'K'
        elif len(threat) > 1:
            threat = sorted(threat, key=lambda x: x[1])
            if threat[-1][1] == threat[-2][1]: answer[i] = 'D'
            else:
                threats[i] = threat[-1]
            
    for i, threat in enumerate(threats):
        if answer[i] == -1:
            temp = []
            next_idx = threat[0][0]
            
            while True:
                temp.append(i)
                if answer[next_idx] != -1:
                    for tem in temp:
                        answer[tem] = next_idx + 1
                    break
                else:
                    next_idx = threats[next_idx][0][0]                
            
    print(f'#{t+1} ', end='')
    print(' '.join(map(str, answer)))