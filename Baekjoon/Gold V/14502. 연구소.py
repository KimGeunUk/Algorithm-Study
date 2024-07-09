import sys
input = sys.stdin.readline

import copy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())

arr = []
blankes = []
viruses = []

for row in range(N):
    ar = list(map(int, input().split()))
    arr.append(ar)
    
    for col in range(M):
        if ar[col] == 0:
            blankes.append((row, col))
        if ar[col] == 2:
            viruses.append((row, col))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = -1

for combi in combinations(blankes, 3):
    arr_copy = copy.deepcopy(arr)
    
    # 새로운 벽
    for row, col in combi:
        arr_copy[row][col] = 1
    
    # 바이러스 퍼짐
    Q = deque(viruses)
    while Q:
        y, x = Q.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if -1 < nx < M and -1 < ny < N and arr_copy[ny][nx] == 0:
                arr_copy[ny][nx] = 2
                Q.append((ny, nx))
    
    cnt = 0
    for ar in arr_copy:
        cnt += ar.count(0)
    
    answer = max(answer, cnt)

print(answer)