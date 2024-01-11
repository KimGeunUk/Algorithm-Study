from collections import defaultdict
def solution(topping):
    answer = 0

    A = defaultdict(int)
    B = defaultdict(int)
    
    for top in topping:
        A[top] += 1
    
    for top in topping[::-1]:
        A[top] -= 1
        if A[top] == 0:
            del(A[top])
            
        B[top] += 1
        
        if len(A) == len(B):
            answer += 1
        
    return answer