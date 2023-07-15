def solution(cards):
    answer = 0
    group = []
    
    index = [i for i in range(len(cards))]
    visited = [0 for _ in range(len(cards))]
    print(index[:3]+index[3+1:])
    
    g = []
    idx = 0
    while True:
        if visited[idx] == 1:
            break
        g.append(cards[idx])        
        idx = cards[idx] - 1
        visited[idx] = 1
    group.append(g)

    return answer

print(solution([8,6,3,7,2,5,1,4])) # 12