def solution(k, score):
    answer = []
    
    L = list()

    for s in score:
        if len(L) < k:
            L.append(s)
            
        elif min(L) < s:
            L.remove(min(L))
            L.append(s)

        answer.append(min(L))
        
    
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200])) # [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])) # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
print(solution(2, [10, 0, 0, 0, 0, 0, 0]))