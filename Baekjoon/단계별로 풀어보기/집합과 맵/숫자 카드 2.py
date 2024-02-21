import sys
input = sys.stdin.readline

from collections import Counter as C

N = int(input())
N_L = list(map(int, input().split()))

M = int(input())
M_L = list(map(int, input().split()))

c = C(N_L)
for m in M_L:
    print(c[m], end=' ')

# import sys
# input = sys.stdin.readline

# from collections import defaultdict

# N = int(input())
# N_L = list(map(int, input().split()))
# N_S = set(N_L)

# M = int(input())
# M_L = list(map(int, input().split()))

# nums = defaultdict(int)
# for n in N_L:
#     nums[n] += 1

# answer = []

# for m in M_L:
#     if m in N_S:
#         answer.append(nums[m])
#     else:
#         answer.append(0)

# print(' '.join(map(str, answer)))