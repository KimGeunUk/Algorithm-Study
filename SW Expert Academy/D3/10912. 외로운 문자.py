T = int(input())

for t in range(T):
    S = list(input().strip())
    
    S.sort()
    
    temp = []
        
    while S:
        if len(S) >= 2:
            p1 = S.pop()
            p2 = S.pop()
        
            if p1 == p2:
                continue
            else:
                temp.append(p1)
                if len(S) == 0: temp.append(p2)
                else: S.append(p2)
        else:
            temp.append(S.pop())
                
    temp.sort()
    print(f'#{t+1} ', end='')
    if temp == []: print('Good')
    else: print(''.join(temp))