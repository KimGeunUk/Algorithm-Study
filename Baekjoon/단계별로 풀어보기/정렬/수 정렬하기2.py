import sys
input = sys.stdin.readline

N = int(input())

L = [0 for _ in range(10001)]

for _ in range(N):
    L[int(input())] += 1

for idx, l in enumerate(L):
    if l != 0:
        for _ in range(1, l+1):
            print(idx)