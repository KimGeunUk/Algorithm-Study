def solution(food):
    answer = []
    
    for idx, num in enumerate(food):
        if idx == 0:
            continue
        
        for _ in range(num//2):
            answer.append(str(idx))
            
    answer.append(str(0))
    
    return ''.join(answer) + ''.join(answer[-2::-1])

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))