import sys
input = sys.stdin.readline

N = int(input())

A = 0
B = 0
sA = 0
sB = 0
last = 0

for _ in range(N):
    team, time = input().split()
    
    m, s = map(int, time.split(":"))
    now = m*60 + s
    
    remain = now - last
    
    if sA > sB:
        A += remain
    elif sB > sA:
        B += remain
        
    if team == '1':
        sA += 1
    else:
        sB += 1
        
    last = now
    
final = 48 * 60
if sA > sB:
    A += final - last
elif sB > sA:
    B += final - last    

for s in [A, B]:
    div, mod = divmod(s, 60)
    print(f"{div:02d}:{mod:02d}")