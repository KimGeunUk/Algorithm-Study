""" 
문제 설명
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

제한사항
arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태를 하고 있습니다. 즉, arr의 행의 개수는 1, 2, 4, 8, ..., 1024 중 하나입니다.
arr의 각 행의 길이는 arr의 행의 개수와 같습니다. 즉, arr은 정사각형 배열입니다.
arr의 각 행에 있는 모든 값은 0 또는 1 입니다.
"""

def rectangle(arr, half):
    global rect
    A, B, C, D = list(), list(), list(), list()
    
    for r_, row in enumerate(arr):
        if r_ < half:
            A.append(row[:half])
            B.append(row[half:])
        else:
            C.append(row[:half])
            D.append(row[half:])

    if A.count(A[0]) == half and A[0].count(A[0][0]) == half:
        A = [A[0][0]]
        if half > 2:
            rect.append(A)
    elif len(A) > 2:
        rectangle(A, half//2)
        
    if B.count(B[0]) == half and B[0].count(B[0][0]) == half:
        B = [B[0][0]]
        if half > 2:
            rect.append(B)
    elif len(B) > 2:
        rectangle(B, half//2)
           
    if C.count(C[0]) == half and C[0].count(C[0][0]) == half:
        C = [C[0][0]]
        if half > 2:
            rect.append(C)
    elif len(C) > 2:
        rectangle(C, half//2)
         
    if D.count(D[0]) == half and D[0].count(D[0][0]) == half: 
        D = [D[0][0]]
        if half > 2:
            rect.append(D)
    elif len(D) > 2:
        rectangle(D, half//2)
        
    # if half <= 2 and A == B == C == D:
    #     rect.append([A[0]])
    if half <= 2:
        rect.append(A)
        rect.append(B)
        rect.append(C)
        rect.append(D)


def solution(arr): 
    global rect
    rect = []
    answer = [0, 0]
    
    r = len(arr)

    half = r // 2
    rectangle(arr, half)
    
    if rect.count(rect[0]) == len(rect) and len(rect[0]) == 1:
        rect = [rect[0]]
    
    for i in rect:
        if len(i) >= 2:
            for j in i:                
                answer[0] += j.count(0)
                answer[1] += j.count(1)
        else:
            answer[0] += i.count(0)
            answer[1] += i.count(1)
            
    return answer

# 다른 사람 풀이
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
            
    check(len(arr),0,0)

    return answer


print(solution([[1,1],
                [1,0]]))

print(solution([[0,1,0,1],
                [0,1,0,1],
                [0,1,0,1],                
                [0,1,0,1]]))

print(solution([[1,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],
                [0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],
                [0,0,0,0,1,1,1,1]]))

print(solution([[1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,0,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]))