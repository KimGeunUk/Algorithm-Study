import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
Q = deque()

for _ in range(N):
    order = input().split()    
    
    if order[0] == 'push':
        Q.append(order[1])
    elif order[0] == 'pop':
        print(-1) if len(Q) == 0 else print(Q.popleft())
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        print(1) if len(Q) == 0 else print(0)
    elif order[0] == 'front':
        print(-1) if len(Q) == 0 else print(Q[0])
    elif order[0] == 'back':
        print(-1) if len(Q) == 0 else print(Q[-1])

# # List로 구현 시 시간초과
# import sys
# input = sys.stdin.readline

# def push(L: list, n: int):
#     return L.append(n)

# def pop(L: list):    
#     return L.pop(0) if len(L) != 0 else -1

# def size(L: list):
#     return len(L)

# def empty(L: list):
#     return 1 if len(L) == 0 else 0

# def front(L: list):
#     return L[0] if len(L) != 0 else -1

# def back(L: list):
#     return L[-1] if len(L) != 0 else -1

# N = int(input())
# L = list()

# for _ in range(N):
#     order = input().split()    
    
#     if order[0] == 'push':
#         push(L, int(order[1]))
#     elif order[0] == 'pop':
#         print(pop(L))
#     elif order[0] == 'size':
#         print(size(L))
#     elif order[0] == 'empty':
#         print(empty(L))
#     elif order[0] == 'front':
#         print(front(L))
#     elif order[0] == 'back':
#         print(back(L))