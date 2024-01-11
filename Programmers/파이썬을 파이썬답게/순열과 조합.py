import itertools
def solution(mylist):
    answer = sorted(list(itertools.permutations(mylist)))
    return answer

import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 순열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 순열 만들기

# 함수
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    print(c)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

print(solution([2, 1]))
print(solution([1, 2, 3]))

print(permute([1,2]))