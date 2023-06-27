def solution(n):
    answer = 0
    
    m = int(n/2)

    for i in range(m):
        if i**2 == n:
            answer = i
    
    if answer == 0:
        return -1
    else:    
        answer = (answer+1)**2
        return answer

    # 시간 초과

def solution2(n):
    answer=0

    m = n//2

    if n == 1:
        return 4
    
    for i in range(2,m):
        if pow(i,2) == n:
            answer = pow(i+1,2)

            return answer
       
    return -1

    # pow(n,m) : n의 m 제곱 리턴
    # import math 모듈 의 sqrt(n) : 제곱근 값

    


print(solution2(121))
print(solution2(3))