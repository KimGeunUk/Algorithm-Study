import sys
input = sys.stdin.readline

K = int(input())
building = list(map(int, input().split()))
graph = [[] for _ in range(K)]

def dfs(building, depth):
    mid = len(building) // 2    
    graph[depth].append(building[mid])
    
    if len(building) == 1: return
    
    dfs(building[:mid], depth+1)
    dfs(building[mid+1:], depth+1)
    
dfs(building, 0)

for nodes in graph:
    print(*nodes)

"""
import sys
input = sys.stdin.readline

K = int(input())
building = list(map(int, input().split()))

len_building = len(building)

for i in range(K):
    n = 2 ** (i + 1)    
    m = (len_building + 1) // n
    
    for j in range(m, len_building+1, m):
        if building[j-1] != -1:
            print(building[j-1], end=' ')
            building[j-1] = -1
    print() 
"""