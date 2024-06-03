import sys
input = sys.stdin.readline

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for info in graph:
    info.sort()


def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for node in graph[start]:
        if visited[node] == False:
            dfs(node)
            

visited = [False for _ in range(N+1)]
dfs(V)
print()


def bfs(start):
    Q = deque([start])
    visited[start] = True
    
    print(start, end=' ')
    while Q:
        p = Q.popleft()
        
        for node in graph[p]:
            if visited[node] == False:
                visited[node] = True
                Q.append(node)
                print(node, end=' ')     
                           
visited = [False for _ in range(N+1)]
bfs(V)
print()