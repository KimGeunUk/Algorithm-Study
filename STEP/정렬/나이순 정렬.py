import sys
input = sys.stdin.readline

N = int(input())

L = [list(input().split()) for _ in range(N)]

print(sorted(L, key=lambda x: int(x[0])))