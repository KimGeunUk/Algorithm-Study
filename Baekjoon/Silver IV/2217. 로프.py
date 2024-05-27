import sys
input = sys.stdin.readline

n = int(input())

ropes = [int(input()) for _ in range(n)]
ropes = sorted(ropes)

max_ = max(ropes)

for i in range(2, n+1):
    max_ = max(ropes[-i] * i, max_)
    
print(max_)