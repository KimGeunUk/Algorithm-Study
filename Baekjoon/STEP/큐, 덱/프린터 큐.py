import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    printer = deque(list(map(int, input().split())))

    count = 0
    while True:            
        max_ = max(printer)        
        
        p = printer.popleft()
        
        if max_ == p:
            if M == 0:
                count += 1
                break
            else:
                N -= 1
                M -= 1             
                count += 1
        else:
            printer.append(p)    
                    
            if M == 0:
                M = N-1
            else:
                M -= 1
        
    print(count)
    
## 
import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
  N, M = map(int, input().split())
  ans = 1
  printer = deque(enumerate(list(map(int, input().split()))))
  
  while True:
    max_tuple = max(printer, key=lambda x:x[1])
    
    p= printer.popleft()
    
    if max_tuple[1] <= p[1]:
      if p[0] == M:
        print(ans)
        break
      else:
        ans += 1
    else:
      printer.append(p)