def solution(elements):
    answer = set()
    
    for i in range(1, len(elements)):
        E = elements + elements[:i-1]
        
        for j in range(len(E)-(i-1)):
            answer.add(sum(E[j:j+i]))
    
    answer.add(sum(elements))
    
    return len(answer)

print(solution([7, 9, 1, 1, 4])) # 18