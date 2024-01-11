from copy import deepcopy
from dis import disco
def solution(want, number, discount):
    answer = 0
    
    if len(discount) < 15:
        discount = discount + discount[:15-len(discount)]
    
    B = dict()
    for w, n in zip(want, number):
        B[w] = n
    T = deepcopy(B)
         
    for i in range(len(discount)-9):
        D = discount[i:i+10]
        for d in D:
            if d not in B or B[d] == 0:
                continue
            B[d] -= 1
        
        if sum(B.values()) == 0:
            answer += 1
            
        B = deepcopy(T)
    
    return answer

from collections import Counter as C
def solution1(want, number, discount):
    answer = 0
    
    B = dict()
    for w, n in zip(want, number):
        B[w] = n
        
    for i in range(len(discount)-9):
        c = C(discount[i:i+10])
        if c == B:
            answer += 1
            
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) # 3

print(solution(["apple"],
               [10],
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) # 0