import sys
input = sys.stdin.readline

def push_front(D, x):
    D = [int(x)] + D
    return D

def push_back(D, x):
    D = D + [int(x)]
    return D

def pop_front(D):
    if len(D) == 0:
        return -1
    else:
        n = D[0]
        D.pop(0)
        return n

def pop_back(D):
    if len(D) == 0:
        return -1
    else:
        n = D[-1]
        D.pop(-1)
        return n
    
def size(D):
    return len(D)

def empty(D):
    return 1 if len(D) == 0 else 0

def front(D):
    if len(D) == 0:
        return -1
    else:
        n = D[0]
        return n

def back(D):
    if len(D) == 0:
        return -1
    else:
        n = D[-1]
        return n

D = list()
N = int(input())

for _ in range(N):
    order = input().split()
    
    if order[0] == 'push_front':
        D = push_front(D, order[1])
    elif order[0] == 'push_back':
        D = push_back(D, order[1])
    elif order[0] == 'pop_front':
        print(pop_front(D))
    elif order[0] == 'pop_back':
        print(pop_back(D))
    elif order[0] == 'size':
        print(size(D))
    elif order[0] == 'empty':
        print(empty(D))
    elif order[0] == 'front':
        print(front(D))
    elif order[0] == 'back':
        print(back(D))