import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
answer = [[0 for _ in range(N)] for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            graph[i].append(j)

def bfs(start):
    Q = deque([start])
    
    while Q:
        p = Q.popleft()
        
        for node in graph[p]:
            if answer[start][node] == 0:
                answer[start][node] = 1
                Q.append(node)
        
for i in range(N):
    bfs(i)

for a in answer:
    print(*a)