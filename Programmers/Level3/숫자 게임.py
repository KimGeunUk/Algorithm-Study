from collections import deque

def solution(A, B):
    answer = 0
        
    A.sort()
    B.sort()

    A = deque(A)
    B = deque(B)

    while A:
        if A[-1] < B[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()

    return answer

print(solution([5,1,3,7], [2,2,6,8])) # 3
print(solution([2,2,2,2], [1,1,1,1])) # 0

print(solution([1,7,7,8], [2,2,6,8])) # 2