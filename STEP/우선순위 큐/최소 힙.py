import sys
input = sys.stdin.readline

from queue import PriorityQueue

N = int(input())
Q = PriorityQueue()

for _ in range(N):
    n = int(input())
    
    if n == 0:
        if Q.qsize() == 0:
            print(0)
        else:
            print(Q.get())
    else:
        Q.put(n)