import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

Q = deque([i for i in range(1, N+1)])

nums = list(map(int, input().split()))

count = 0
for n in nums:
    while True: 
        p = Q.popleft()
        
        if p == n:
            break
        else:
            Q.appendleft(p)
            
            n_index = Q.index(n)
            if n_index <= len(Q) // 2:
                Q.rotate(-n_index)
                count += n_index           
            else:                
                Q.rotate(len(Q) - n_index)       
                count += len(Q) - n_index
print(count)