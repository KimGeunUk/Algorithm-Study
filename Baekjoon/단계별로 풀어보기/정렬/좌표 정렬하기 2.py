import sys
input = sys.stdin.readline

N = int(input())

L = [list(map(int, input().split())) for _ in range(N)]

for l in sorted(L, key=lambda x: (x[1], x[0])):
    print(l[0], l[1])