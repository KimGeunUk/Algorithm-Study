
def solution(mylist):
    answer = []
    
    for i, j in zip(mylist[:-1], mylist[1:]):
        answer.append(abs(i-j))        
    
    return answer

print(solution([83, 48, 13, 4, 71, 11]))