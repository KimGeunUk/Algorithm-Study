import sys
input = sys.stdin.readline

N, M = map(int, input().split())

L = list(map(int, input().split()))

array = [0 for _ in range(N+1)]

c = 0

for i in range(1, N+1):
    array[i] = (L[i-1] + array[i-1]) % 3

print(array)