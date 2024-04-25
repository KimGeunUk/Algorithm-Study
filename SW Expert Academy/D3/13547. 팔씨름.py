T = int(input())

for t in range(T):
    string = input().strip()
    
    x = 0

    for s in string:
        if s == 'x': x += 1
    
    if 15 - x >= 8: print(f'#{t+1} YES')
    else: print(f'#{t+1} NO')