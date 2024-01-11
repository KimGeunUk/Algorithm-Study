import sys
input = sys.stdin.readline

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # -10,000 <= x1, y1, x2, y2 <= 10,000 / r1, r2 <= 10,000
    
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if d == 0 and r1 == r2: # 원 이 같을 때
        print(-1)
    elif abs(r1 - r2) < d and abs(r1 + r2) > d: # 두 원이 두 점에서 만날때
        print(2)
    elif abs(r1 + r2) == d or abs(r1 - r2) == d: # 내접 or 외접
        print(1)
    elif abs(r1 + r2) < d or abs(r1 - r2) > d or (d == 0 and r1 != r2): # 두 원이 접하지 않을 때
        print(0)
