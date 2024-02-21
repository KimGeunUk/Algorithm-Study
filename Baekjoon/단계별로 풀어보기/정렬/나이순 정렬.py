import sys
input = sys.stdin.readline

N = int(input())

L = [list(input().split()) for _ in range(N)]

for l in sorted(L, key=lambda x: int(x[0])):
    print(l[0], l[1])