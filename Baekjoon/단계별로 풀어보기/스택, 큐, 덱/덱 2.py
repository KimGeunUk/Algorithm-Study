import sys
input = sys.stdin.readline

from collections import deque

D = deque()

n = int(input())

for _ in range(n):
    cmd = input().strip().split()
    
    if cmd[0] == '1':
        D.appendleft(cmd[1])
    elif cmd[0] == '2':
        D.append(cmd[1])
    elif cmd[0] == '3':
        if D: print(D.popleft())
        else: print(-1)
    elif cmd[0] == '4':
        if D: print(D.pop())
        else: print(-1)
    elif cmd[0] == '5':
        print(len(D))
    elif cmd[0] == '6':
        if D: print(0)
        else: print(1)
    elif cmd[0] == '7':
        if D: print(D[0])
        else: print(-1)
    elif cmd[0] == '8':
        if D: print(D[-1])
        else: print(-1)