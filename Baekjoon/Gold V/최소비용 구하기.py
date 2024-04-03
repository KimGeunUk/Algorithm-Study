import sys
input = sys.stdin.readline

import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [float('inf') for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

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

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])