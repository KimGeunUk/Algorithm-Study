def solution(numbers):
    answer = [-1] * len(numbers)    
    s = []
    
    for idx, n in enumerate(numbers):
        while s and numbers[s[-1]] < n:
            answer[s.pop()] = n
        s.append(idx)
    return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if numbers[j] >= numbers[i]: 
                break
            answer[j] = numbers[i]
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))