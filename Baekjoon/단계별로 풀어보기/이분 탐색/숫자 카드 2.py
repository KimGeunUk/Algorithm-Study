import sys
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

maps = defaultdict(lambda: 0)

for a in A:
    maps[a] += 1
    
for b in B:
    if b in maps:
        print(maps[b], end=' ')
    else:
        print(0, end=' ')