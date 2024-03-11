import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())    
    L = input().rstrip()[1:-1].split(',')
    
    if n == 0:
        Q = deque()
    else:
        Q = deque(L)
        
    R_c = 0 # R의 개수
    
    for p_ in p:
        if p_ == 'R':
            R_c += 1
        else:
            if len(Q) != 0:
                if R_c % 2 == 0:
                    Q.popleft()
                else:
                    Q.pop() 
            else:
                Q = -1
                break
    
    if Q != -1:
        if R_c % 2 == 0:
            print('[' + ','.join(map(str, Q))+']')
        else:
            Q.reverse()
            print('[' + ','.join(map(str, Q))+']')
    else:
        print('error')