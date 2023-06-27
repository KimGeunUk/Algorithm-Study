from itertools import combinations as cb # List에서 n만큼 원소 뽑기(중복 X)
def solution(number):
    answer = 0
    
    for c in cb(number, 3):
        if sum(c) == 0:
            answer += 1
    
    return answer

print(solution([-2, 3, 0, 2, -5])) # 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 5
print(solution([-1, 1, -1, 1])) # 0