# import sys
# input = sys.stdin.readline

# N = int(input())

# SCENE = [list(input().rstrip()) for _ in range(N)]

# def Check(scene, n, answer):
#     c_0 = 0
#     for s in scene:
#         c_0 = c_0 + s.count('0')

#     if c_0 == 0 or c_0 == n**2:                
#         if c_0 == 0:
#             answer.append(1)
#         else:
#             answer.append(0)
#         return
#     else:
#         for _ in range(4):
#             answer.append([])
       
#         scene1 = [s[:n//2] for s in scene[:n//2]]
#         Check(scene1, n//2, answer[0])
#         scene2 = [s[n//2:] for s in scene[:n//2]]
#         Check(scene2, n//2, answer[1])
#         scene3 = [s[:n//2] for s in scene[n//2:]]
#         Check(scene3, n//2, answer[2])
#         scene4 = [s[n//2:] for s in scene[n//2:]]
#         Check(scene4, n//2, answer[3])

# answer = []
# Check(SCENE, N, answer)

# import re

# a = str(answer)
# a = re.sub('\[(\d)\]', '\\1', a) # [숫자] -> [] 제거
# a = re.sub(',\s*', '', a) # , 공백 -> 제거
# a = re.sub('\[', '(', a) # [ -> (
# a = re.sub('\]', ')', a) # ] -> )

# print(a)

import sys
input = sys.stdin.readline

N = int(input())

SCENE = [list(input().rstrip()) for _ in range(N)]

def Check(scene, n):
    c_0 = 0    
    for s in scene:
        c_0 = c_0 + s.count('0')
        
    if c_0 == 0 or c_0 == n**2:
        if c_0 == 0:
            print(1, end="")
        else:           
            print(0, end="")
        return
    else:
        print("(", end="")       
        scene1 = [s[:n//2] for s in scene[:n//2]]
        Check(scene1, n//2)
        scene2 = [s[n//2:] for s in scene[:n//2]]
        Check(scene2, n//2)
        scene3 = [s[:n//2] for s in scene[n//2:]]
        Check(scene3, n//2)
        scene4 = [s[n//2:] for s in scene[n//2:]]
        Check(scene4, n//2)
        
        print(")", end="")

Check(SCENE, N)

##
##
