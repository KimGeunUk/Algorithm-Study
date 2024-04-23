def xor(a, b):
    a, b = a % 2, b % 2
    
    if a == 0 and b == 0: return 0
    elif a == 1 and b == 1: return 0
    elif a == 0 and b == 1: return 1
    elif a == 1 and b == 0: return 1

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    
    maps = [list(map(int, list(input().strip()))) for _ in range(n)]
    trigger = True
    
    for i in range(n):
        if not trigger: break
        
        for j in range(m):
            if xor(i, j) != maps[i][j]:
                trigger = False
                break
    
    if trigger:
        print(f'#{t+1} yes')
    else:
        print(f'#{t+1} no')