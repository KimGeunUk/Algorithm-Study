import sys
input = sys.stdin.readline

from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cntDict = defaultdict(int)
max_ = -1

st = 0
ed = 0
while ed < N:
    cntDict[arr[ed]] += 1
    
    while cntDict[arr[ed]] > K:
        cntDict[arr[st]] -= 1
        st += 1
    
    ed += 1
    max_ = max(max_, ed - st)

print(max_)