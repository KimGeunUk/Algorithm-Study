import sys
input = sys.stdin.readline

def push(L: list, n: int):
    return L.append(n)

def pop(L: list):    
    return L.pop() if len(L) != 0 else -1

def size(L: list):
    return len(L)

def empty(L: list):
    return 1 if len(L) == 0 else 0

def top(L: list):
    return L[-1] if len(L) != 0 else -1

N = int(input())
L = list()

for _ in range(N):
    order = input().rstrip()    
    
    if order[:4] == 'push':
        push(L, int(order[5:]))
    elif order == 'top':
        print(top(L))
    elif order == 'size':
        print(size(L))
    elif order == 'empty':
        print(empty(L))
    elif order == 'pop':
        print(pop(L))