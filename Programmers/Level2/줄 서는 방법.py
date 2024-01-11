""" 
문제 설명
n명의 사람이 일렬로 줄을 서고 있습니다. 
n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다.
n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

제한사항
n은 20이하의 자연수 입니다.
k는 n! 이하의 자연수 입니다.
"""

from math import factorial

def solution(n, k):
    answer = []
    num = list(range(1, n+1))
    fac = factorial(n)

    i = 1
    for idx, n_ in enumerate(range(n, 0, -1)):
        i *= n_
        nums = fac // i
        
        now = k // nums
        k = k % nums
        
        if k == 0:
            answer.append(num[now-1])
            num.remove(num[now-1]) 
        else:
            answer.append(num[now])
            num.remove(num[now]) 

    return answer

from itertools import permutations

def solution1(n, k):
    return list(permutations(range(1, n+1), n))[k-1]

#print(solution(3, 5)) # [1, 2, 3] # [3, 1, 2]
#print(solution(5, 15)) # [1, 2, 3, 4, 5] # [1, 4, 3, 2, 5] 
print(solution(3, 2)) # [1, 2, 3, 4] # [2, 3, 4, 1] 