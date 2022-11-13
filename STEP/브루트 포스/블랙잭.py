import sys
input = sys.stdin.readline

from itertools import combinations as c

N, M = map(int, input().split())
L = list(map(int, input().split()))

min = float('inf')
answer = 0

for c_ in c(L, 3):
    if  M - sum(c_) >= 0 and M - sum(c_) < min:
        min = abs(sum(c_) - M)

print(M - min)