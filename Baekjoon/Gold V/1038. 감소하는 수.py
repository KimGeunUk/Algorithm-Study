import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
now = 0

while True:
    if cnt == N:
        print(now)
        break
    
    if now > 1000000:
        print(-1)
        break

    if now < 10:
        cnt += 1
        now += 1
        continue
    
    temp = now
    next_ = 10
    
    trigger = True
    while temp > 0:
        prev_ = temp % 10
        if prev_ >= next_:
            trigger = False
            break
        
        next_ = prev_
        temp //= 10

    if trigger:
        cnt += 1
        
    now += 1
    
    print(now, cnt, trigger)