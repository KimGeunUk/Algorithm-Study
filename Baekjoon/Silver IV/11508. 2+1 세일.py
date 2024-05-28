import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

answer = 0

for i, ar in enumerate(arr):
    if i % 3 == 2: continue
    answer += ar

print(answer)