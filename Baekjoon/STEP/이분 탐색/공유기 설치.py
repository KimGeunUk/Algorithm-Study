import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
x = sorted(x)

start = 1
end = x[-1] - x[0]
answer = 0

while start <= end:
    mid = (start+end)//2    # 최대 거리
    
    cnt = 1
    now_ = x[0]
    for i in range(1, N):
        if x[i] - now_ >= mid:
            cnt += 1
            now_ = x[i]
        
    if cnt >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1    
        
print(answer)