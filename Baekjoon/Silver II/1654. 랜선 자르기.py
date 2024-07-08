import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

st = 1
ed = max(lans)

while st <= ed:
    mid = (st + ed) // 2
    
    cnt = 0    
    for lan in lans:
        cnt += lan // mid
        
    if cnt >= N:
        st = mid + 1
    else:
        ed = mid - 1

print(ed)