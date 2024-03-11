import sys
input = sys.stdin.readline

from collections import deque

answer = []

n = int(input())

D = deque(list(enumerate(map(int, input().split()), start=1)))

index, paper = D.popleft()
answer.append(index)

while D:
    if paper > 0:
        for _ in range(paper-1):
            p = D.popleft()
            D.append(p)
        index, paper = D.popleft()
    elif paper < 0:
        for _ in range(abs(paper) - 1):
            p = D.pop()
            D.appendleft(p)
        index, paper = D.pop()
    
    answer.append(index)

print(' '.join(map(str, answer)))

# 다른 사람 풀이
answer = []

n = int(input())

D = deque(list(enumerate(map(int, input().split()), start=1)))

while D:
    index, paper = D.popleft()
    answer.append(index)
    
    if paper > 0:
        D.rotate(-(paper-1))
    elif paper < 0:
        D.rotate(-paper)
        
print(' '.join(map(str, answer)))

