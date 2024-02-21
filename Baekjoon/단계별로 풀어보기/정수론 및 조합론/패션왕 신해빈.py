import sys
input = sys.stdin.readline

from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    D = defaultdict(int)
    
    answer = 1
    
    for _ in range(N):
        n, c = map(str, input().split())
        D[c] += 1

    for v in D.values():
        answer *= v + 1    
    
    print(answer-1)