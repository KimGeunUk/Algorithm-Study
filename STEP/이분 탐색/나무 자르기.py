import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start+end)//2
    
    s = 0
    for tree in trees:
        r = tree - mid
        if r > 0:
            s += r
        if s > M:
            break     
        
    if s >= M:
        start = mid + 1
    else:
        end = mid - 1    
        
print(end)