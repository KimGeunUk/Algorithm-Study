import sys
input = sys.stdin.readline

def binary(LIST, target, start, end):
    while start <= end:
        m = (start + end) // 2
        if LIST[m] == target:
            return 1
        elif LIST[m] > target:
            end = m - 1
        else:
            start = m + 1
    return 0

N = int(input()) # 1 <= N <= 500,000
N_L = list(map(int, input().split())) # -10,000,000 <= a <= 10,000,000

M = int(input())
M_L = list(map(int, input().split()))

N_L.sort()

for m in M_L:
    print(binary(N_L, m, 0, N-1), end=' ')

# import sys
# input = sys.stdin.readline

# N = int(input()) # 1 <= N <= 500,000
# N_L = list(map(int, input().split())) # -10,000,000 <= a <= 10,000,000
# N_S = set(N_L)

# M = int(input())
# M_L = list(map(int, input().split())) 
# M_S = set(M_L) 

# intersection = N_S & M_S
# answer = []

# for idx, m in enumerate(M_L):
#     if m in intersection:
#         answer.append(1)
#     else:
#         answer.append(0)

# print(' '.join(map(str, answer)))
