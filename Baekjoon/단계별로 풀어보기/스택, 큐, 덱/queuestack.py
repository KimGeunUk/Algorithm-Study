import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
M = int(input())
C = list(map(int, input().strip().split()))

Z = deque()
for a, b in zip(A, B):
    if a == 0:
        Z.append(b)

for c in C:
    if Z:            
        p = Z.pop()
        Z.appendleft(c)        
        print(p, end=' ')
    else:
        print(c, end=' ')