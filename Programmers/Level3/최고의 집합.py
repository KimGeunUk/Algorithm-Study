def solution(n, s):
    answer = []
    
    """
    1. 각 원소의 합이 S가 되는 수의 집합
    2. 위 조건을 만족하면서 각 원소의 곱이 최대가 되는 집합    
    """
    
    # 중간에 있는 값들이 젤 곱이 큼 -> 나누기 n
    
    while s > 0:
        if s//n == 0:
            return [-1]
        
        answer.append(s//n)
        s -= s//n
        n -= 1

   
    return answer

print(solution(2, 9)) # [4, 5]
print(solution(2, 1)) # [-1]
print(solution(2, 8)) # [4, 4]
print(solution(3, 9)) # [4, 5]