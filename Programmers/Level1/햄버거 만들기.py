def solution(ingredient):
    answer = 0
    idx = 0

    while True:
        if ingredient[idx:idx+4] == [1, 2, 3, 1]:
            del ingredient[idx:idx+4]
            answer += 1
            idx -= 4
        else:
            idx += 1

        if idx == len(ingredient):
            break

    return answer

def solution(ingredient):
    answer = 0
    
    temp = []
    for i in ingredient:
        temp.append(i)
        
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            del temp[-4:]
            
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2])) # 0
print(solution([2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3, 1, 3, 1]))