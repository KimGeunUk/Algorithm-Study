import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ranks = [list(map(int, input().split())) for _ in range(N)]

ranks.sort(key=lambda x: (-x[1], -x[2], -x[3]))

cnt = 1
tmp = 0
previous = ranks[0][1:]

if ranks[0][0] == K:
    print(1)
else:
    for rank in ranks[1:]:
        now = rank[1:]
        
        if previous == now:
            tmp += 1
        else:        
            cnt += tmp + 1
            tmp = 0        
            previous = now
        
        if rank[0] == K: break

    print(cnt)