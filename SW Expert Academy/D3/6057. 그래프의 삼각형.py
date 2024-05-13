from collections import defaultdict
from itertools import combinations

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    D = defaultdict(list)
    
    for _ in range(M):
        x, y = map(int, input().split())
        x, y = min(x, y), max(x, y)
        
        D[x].append(y)

    count = 0
    for v in D.values():
        if len(v) >= 2:
            C = combinations(v, 2)
            for c in C:
                x, y = min(c), max(c)
                if x in D.keys() and y in D[x]:
                    count += 1
    
    print(f'#{t+1} {count}')