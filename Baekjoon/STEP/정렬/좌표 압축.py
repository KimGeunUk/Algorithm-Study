import sys
input = sys.stdin.readline

N = int(input())

L = list(map(int, input().split()))
L_ = list(sorted(set(L)))

D = {L_[i]: i for i in range(len(L_))}
for l in L:
    print(D[l], end=' ')