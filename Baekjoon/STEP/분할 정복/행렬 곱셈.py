import sys
input = sys.stdin.readline

A, B = list(), list()

N, M = map(int, input().split())

for _ in range(N):
    A.append(list(map(int, input().split())))
    
M, K = map(int, input().split())

for _ in range(M):
    B.append(list(map(int, input().split())))
    
answer = [[] for _ in range(N)]

for r in range(N):
    for c in range(K):
        s = 0
        for a, b in zip(A[r], B[:]):
            s += a * b[c]
        answer[r].append(s)
        
for a in answer:
    print(*a)