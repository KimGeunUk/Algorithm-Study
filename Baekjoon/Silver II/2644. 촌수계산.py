import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

parent_child = defaultdict(list)
child_parent = dict()

for _ in range(m):
    x, y = map(int, input().split())
    
    parent_child[x].append(y)
    child_parent[y] = x

def bfs(x, count):
    Q = deque([(x, 0)])
    visited = set()
    
    while Q:        
        x, count = Q.popleft()
        
        if x == b:
            return count
        
        if x not in visited:
            visited.add(x)
            
            childs = parent_child[x]
            for child in childs:
                if child not in visited:
                    Q.append((child, count+1))
  
            if x in child_parent.keys():
                parent = child_parent[x]
                if parent not in visited:     
                    Q.append((parent, count+1))

    return -1

print(bfs(a, 0))