import heapq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [float('inf') for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append((e[1], 1))
        graph[e[1]].append((e[0], 1))

    def dijkstra(start):
        Q = []
        heapq.heappush(Q, (0, start))
        distance[start] = 0
        
        while Q:
            dist, now = heapq.heappop(Q)
            
            if distance[now] < dist: continue
            
            for i in graph[now]:
                cost = dist + i[1]
                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(Q, (cost, i[0]))
    
    dijkstra(1)
    
    return distance[1:].count(max(distance[1:]))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3
print(solution(4, [[4, 3], [1, 3], [2, 3]])) # 2

