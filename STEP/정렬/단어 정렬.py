from cProfile import label
import sys
input = sys.stdin.readline

N = int(input())

L = [input().rstrip() for _ in range(N)]
L = list(set(L))
L = sorted(L, key=lambda x: (len(x), x))
print(L)