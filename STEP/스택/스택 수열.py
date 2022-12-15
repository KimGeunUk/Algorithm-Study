# import sys
# input = sys.stdin.readline

# N = int(input())

# nums = [i for i in range(N, 0, -1)]

# u = list()
# o = list()

# command = list()
# inputs = list()

# for _ in range(N):    
#     n = int(input())        
#     if len(u) == 0 or u[-1] < n:        
#         for i in nums[::-1]:
#             if i <= n:                
#                 u.append(nums.pop())
#                 command.append('+')
#             else:
#                 if len(u) == 0:
#                     break
#                 else:
#                     o.append(u.pop())
#                     command.append('-')
#                     break
#     else:
#         for i in u[::-1]:
#             if i >= n:
#                 if len(u) == 0:
#                     break
#                 else:
#                     o.append(u.pop())
#                     command.append('-')
#             else:
#                 break
# else:
#     if len(u) > 0:
#         for i in u:
#             o.append(u.pop())
#             command.append('-')

# if inputs != o:
#     print("NO")
# else:
#     for i in command:
#         print(i)

import sys
input = sys.stdin.readline

n = int(input())
stack, answer = [], []
is_can, cur = True, 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        is_can = False
        break
    
if is_can:
    for i in answer:
        print(i)