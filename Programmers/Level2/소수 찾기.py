import math

def is_primenum(x):    
    if x == 0 or x == 1:
        return False    
    # 2부터 x의 제곱근 까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False    
    return True

import itertools

def solution(numbers):
    answer = 0
    answer_dict = {}
    a = set()
    
    number = [i for i in numbers]
    for j in range(1, len(number)+1):
        for i in itertools.permutations(number, j):
            answer_dict[int(''.join(i))] = 1
            
        # 바로 위의 코드를 다음과 같이 수정하면 best - != 는 update 개념
        # a |= set(map(int, map("".join, itertools.permutations(list(numbers), j))))
    
    for i in answer_dict.keys():
        if is_primenum(i) == True:
            answer += 1

    return answer

# 다른 사람 풀이 - 재귀
# primeSet = set()

# def isPrime(number):
#     if number in (0, 1):
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True


# def makeCombinations(str1, str2):
#     if str1 != "":
#         if isPrime(int(str1)):
#             primeSet.add(int(str1))

#     for i in range(len(str2)):
#         makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


# def solution(numbers):
#     makeCombinations("", numbers)

#     answer = len(primeSet)

#     return answer

print(solution("17"))
print(solution("011"))