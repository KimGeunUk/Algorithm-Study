""" 
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건 : 
    행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
    행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
    곱할 수 있는 배열만 주어집니다.
"""
import numpy as np
def solution(arr1, arr2):    
    answer = np.dot(arr1, arr2)

    return np.ndarray.tolist(answer)

def solution1(arr1, arr2):
    answer = []
    
    for y1 in range(len(arr1)):
        a = []
        for x2 in range(len(arr2[0])):
            n = 0
            for x1 in range(len(arr1[0])):
                n += arr1[y1][x1] * arr2[x1][x2]
            a.append(n)
        answer.append(a)
        
    return answer

# 다른 사람 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))