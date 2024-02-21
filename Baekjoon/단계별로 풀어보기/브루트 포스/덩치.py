import sys
input = sys.stdin.readline

N = int(input())

L = list()
for _ in range(N):
    L.append(list(map(int, input().split())))

answer = [1 for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if L[i][0] > L[j][0] and L[i][1] > L[j][1]:
            answer[j] += 1
        elif L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            answer[i] += 1

print(' '.join(map(str, answer)))