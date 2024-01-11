def solution(cards):
    group = []
    visited = [False for _ in range(len(cards)+1)]
    
    for num in cards:
        if not visited[num]:
            temp = []
            while True:
                if num in temp:
                    break
                temp.append(num)                
                visited[num] = True
                num = cards[num-1]
            
            group.append(len(temp))
            
    group = sorted(group, reverse=True)    

    if len(group) < 2:
        return 0
    else: 
        return group[0] * group[1]

print(solution([8,6,3,7,2,5,1,4])) # 12
print(solution([1, 1])) # 12