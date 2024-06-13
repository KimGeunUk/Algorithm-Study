import sys
input = sys.stdin.readline

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

max_ = max(money)
start = min(money)
end = sum(money)

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    remain = mid
    
    for m in money:
        if remain < m:
            remain = mid
            cnt += 1
        remain -= m
    
    if cnt > M or mid < max_:
        start = mid + 1
    else:
        end = mid - 1

print(start)