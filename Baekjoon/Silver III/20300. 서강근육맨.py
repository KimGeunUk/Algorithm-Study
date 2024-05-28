import sys
input = sys.stdin.readline

n = int(input())
T = list(map(int, input().split()))
T.sort()

max_ = -1

if n % 2 == 1: max_ = T.pop()

if T:
    for i in range(n//2+1):
        max_ = max(T[i]+T[-i-1], max_)

print(max_)