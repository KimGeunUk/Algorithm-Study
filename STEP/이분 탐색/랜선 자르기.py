import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    
    s = 0
    for l in lan:
        s += l // mid
        
    if s >= N:
        start = mid + 1
    else:
        end = mid - 1    
        
print(end)