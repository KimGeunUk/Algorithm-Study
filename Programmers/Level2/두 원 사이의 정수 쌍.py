import math

def solution(r1, r2):
    answer = 0
    
    for i in range(1, r2 + 1):
        r1_y = math.ceil(math.sqrt(math.pow(r1, 2) - math.pow(i, 2))) if r1 > i else 0
        r2_y = math.floor(math.sqrt(math.pow(r2, 2) - math.pow(i, 2)))
        
        answer += r2_y - r1_y + 1

    return answer * 4

print(solution(1, 3)) # 28
print(solution(2, 3)) # 20