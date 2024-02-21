import sys
input = sys.stdin.readline

N, M = map(int, input().split())

LIST = [list(map(int, input().split())) for _ in range(N)]
SUM = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        SUM[i][j] = SUM[i][j-1] + SUM[i-1][j] - SUM[i-1][j-1] + LIST[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(SUM[x2][y2] - SUM[x1-1][y2] - SUM[x2][y1-1] + SUM[x1-1][y1-1])


# 시간 초과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# L = list()
# for _ in range(N):
#     L += list(map(int, input().split())) 

# array = [0 for _ in range((N*N)+1)]

# for i in range(1, (N*N)+1):
#     array[i] = sum(L[:i])

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
    
#     s = 0
#     for i in range(x1-1, x2):
#         s += array[(N*i)+y2] - array[(N*i)+y1-1]
#     print(s)