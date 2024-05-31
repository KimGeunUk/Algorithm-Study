import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = list()
D = dict()

for n in range(N):
    word = input().rstrip()
    L.append(word)
    D[word] = n + 1

for _ in range(M):
    word = input().rstrip()
    if word[0].isdecimal():
        print(L[int(word)-1])
    else:
        print(D[word])
