import sys
input = sys.stdin.readline

N, D = map(int, input().split())

dp = [float('inf')] * (D + 1)
dp[0] = 0

shortcuts = []
for _ in range(N):
    start, end, cost = map(int, input().split())
    if end <= D:
        shortcuts.append((start, end, cost))

shortcuts.sort(key=lambda x: x[1])

for i in range(1, D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)

    for start, end, cost in shortcuts:
        if end == i and dp[start] + cost < dp[end]:
            dp[end] = dp[start] + cost

print(dp[D])


"""
import sys
input = sys.stdin.readline

import heapq

def dijkstra(start):
    q = []    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        now_cost, now_node = heapq.heappop(q)
        
        if distance[now_node] < now_cost: continue
        
        for next_node, next_cost in graph[now_node]:            
            next_cost = now_cost + next_cost
            
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))


N, D = map(int, input().split())
graph = [[(i+1, 1)] for i in range(D)]
graph.append([])
distance = [float('inf') for _ in range(D+1)]

for _ in range(N):
    start, end, cost = map(int, input().split())
    if end > D: continue
    graph[start].append((end, cost))

dijkstra(0)

print(distance[D])
"""