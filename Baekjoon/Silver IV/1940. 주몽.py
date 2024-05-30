import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N - 1

count = 0
while start < end:
    sum_ = arr[start] + arr[end]
    
    if sum_ < M:
        start += 1
    elif sum_ > M:
        end -= 1
    elif sum_ == M:
        start += 1
        end -= 1
        count += 1

print(count)

"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

visited = [0 for _ in range(10000001)]

for ar in arr:
    visited[ar] += 1
    
count = 0
for ar in arr:
    if visited[M-ar] > 0:
        visited[M-ar] -= 1
        if visited[ar] > 0:
            visited[ar] -= 1
            count += 1
            
print(count)
"""