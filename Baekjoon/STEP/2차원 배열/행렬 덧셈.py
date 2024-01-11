import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1, arr2 = [], []

for arr in [arr1, arr2]:
    for _ in range(N):
        arr.append(list(map(int, input().split())))

for n in range(N):
    temp = ''
    for m in range(M):
        temp += str(arr1[n][m] + arr2[n][m]) + ' '
    print(temp) 