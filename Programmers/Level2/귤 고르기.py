from collections import Counter as C

def solution(k, tangerine):
    answer = 0
    
    for c in C(tangerine).most_common():
        k -= c[1] 
        
        answer += 1
        
        if k <= 0:
            break

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1