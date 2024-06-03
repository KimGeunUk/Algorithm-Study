import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        p = queue.popleft()
        
        for node in graph[p]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        count += 1
        
print(count)


"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

count = N
status = [i for i in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())

    if status[u] != status[v]:
                    
        if status[u] < status[v]:  
            before = status[v]
            after = status[u]
        else:
            before = status[u]
            after = status[v]
            
        for i in range(1, N+1):
            if status[i] == before:
                status[i] = after
            elif status[i] > before:
                status[i] -= 1

        count -= 1

print(count)

"""