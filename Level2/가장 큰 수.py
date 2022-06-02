import itertools
import math

# 내풀이 - 시간초과
# def solution(numbers):    
#     answer = ''
    
#     str_numbers = [str(i) for i in numbers]
    
#     #num_sort = sorted(str_numbers, key=lambda x: ([-int(x[i]) for i in range(len(x))]))
#     num_sort = sorted(str_numbers, key=lambda x: (-int(x[0])))
    
#     for i in range(len(num_sort)-1):
#         tmp = ''
#         for j in range(i+1, len(num_sort)):
#             if len(num_sort[i]) == len(num_sort[j]):
#                 pass
#             elif num_sort[i][0] == num_sort[j][0]:
#                 if int(num_sort[i] + num_sort[j]) < int(num_sort[j] + num_sort[i]):
#                     tmp = num_sort[i]
#                     num_sort[i] = num_sort[j]
#                     num_sort[j] = tmp   

#     num_sort = int(''.join(num_sort))

#     return str(num_sort)

# 다른 사람 풀이
# def solution(numbers):
#     answer = ''
#     sum_ = 0
#     tmp = []
#     for number in numbers:
#         c = (str(number) * 3)[:3]
#         length = len(str(number))
#         tmp.append((c, length))
#     tmp.sort(reverse=True)
#     for (c, length) in tmp:
#         sum_ += int(c)
#         if sum_ == 0:
#             return '0'
#         answer += c[:length]
#     return answer

# 다른 사람 풀이
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

# 다른 사람 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0]))
print(solution([9, 998]))
print(solution([30, 3021]))