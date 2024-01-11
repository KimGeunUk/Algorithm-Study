""" 
문제 설명
정수 n이 매개변수로 주어집니다.
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
"""
from itertools import chain
def solution(n):
    answer = [[[] for _ in range(room) ] for room in range(n+1)]
    
    i = n
    line = 1
    level =1
    
    while True:
        if line == 1:
            k = 1
        else:
            k = k_ + 1
            
        for i_ in range(k, k+i):
            answer[line][level-1].append(i_)
            line += 1
            
        i -= 1
        if i == 0:
            break
        
        for idx, j_ in enumerate(range(i_+1, i_+i+1)):
            answer[line-1][level+idx].append(j_)
        
        i -= 1
        if i == 0:
            break
        
        for k_ in range(j_+1, j_+i+1):
            line -= 1
            answer[line-1][-level].append(k_)
        
        i -= 1
        if i == 0:
            break
        
        level += 1
            
    return list(chain(*list(chain(*answer))))

print(solution(4)) # [1,2,9,3,10,8,4,5,6,7] # 10
print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9] # 15
#print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11] # 21
print(solution(10)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11] # 21