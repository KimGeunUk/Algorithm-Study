N = int(input())
K = int(input())

start = 1
end = N*N

while start <= end:
    mid = (start+end)//2    # 최대 거리
    
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
        
    if cnt < K:
        start = mid + 1
    else:
        end = mid - 1    
        
print(start)