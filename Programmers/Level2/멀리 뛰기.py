""" 
문제 설명
효진이는 멀리 뛰기를 연습하고 있습니다. 
효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는

(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)

의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 
멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 
여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

제한 사항 : 
    n은 1 이상, 2000 이하인 정수입니다.
"""

from collections import Counter
from math import factorial
def solution(n):
    answer = 1
    
    L = list()
    
    c = 1
    while True:
        l = list()
        
        [l.append(2) for i in range(c)]            
        m = n - 2 * c
        
        if m < 0:
            break
        
        [l.append(1) for i in range(m)]        
        c+=1        
        L.append(l)
    
    # / 보단 // 사용을 하자
    for i in L:
       C = Counter(i)
       s = factorial(C[1] + C[2]) // (factorial(C[1])*factorial(C[2]))
       answer += int(s)
        
    return answer % 1234567

# 다른 사람 풀이 - 피보나치..!
def solution1(n):
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b

print(solution1(2000))
print(solution1(4))
print(solution1(3))