T = int(input())

for t in range(T):
    arr = [list(input().strip()) for _ in range(8)]
    
    trigger = 'yes'
    
    for ar in arr:
        count = 0
        for a in ar:
            if a == 'O': count += 1
        
        if count != 1:
            trigger = 'no'
            break
    
    arr = list(map(list, zip(*arr)))
    
    for ar in arr:
        count = 0
        for a in ar:
            if a == 'O': count += 1
        
        if count != 1:
            trigger = 'no'
            break
        
    print(f'#{t+1} {trigger}')
            