import math
T = int(input())
 
for t in range(T):
    N = int(input())
     
    L = []
     
    for r in range(N):
        col = list(input().strip())
        for c in range(N):
            if col[c] == '1':
                L.append([r+1, c+1])
         
    if L:            
        trigger = False
        for i in range(1001):
            if trigger == True:
                print(f'#{t+1} YES')
                break
             
            for l in L:
                if math.gcd(l[0]+i, l[1]+i) != 1:
                    break
            else:
                trigger = True
        else:
            print(f'#{t+1} NO')
    else:
        print(f'#{t+1} NO')