import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = list(map(int, input().split()))

array = [0 for _ in range(N+1)]

for i in range(1, N+1):
    array[i] = L[i-1] + array[i-1]

for _ in range(M):
    i, j = map(int, input().split())    
    print(array[j] - array[i-1])

# array = [[0 for _ in range(i)] for i in range(1, N+1)]

# for i in range(N):
#     for j in range(i, -1, -1):
#         if i == j:
#             array[i][j] = L[i]
#         else:
#             array[i][j] = array[i-1][j] + L[i]

# for _ in range(M):
#     i, j = map(int, input().split())    
#     print(array[j-1][i-1])
    
#    5  4  3  2  1
# 5  5  9 12 14 15
# 4  0  4  7  9 10
# 3  0     3  5  6
# 2  0        2  3
# 1  0           1