import sys
input = sys.stdin.readline

N, K = map(int, input().split())

L = list(map(int, input().split()))

array = [0 for _ in range(N+1)]

for i in range(1, N+1):
    array[i] = L[i-1] + array[i-1]

max_ = -float('inf')
for i in range(K, N+1):
    max_ = max(array[i] - array[i-K], max_)
print(max_)