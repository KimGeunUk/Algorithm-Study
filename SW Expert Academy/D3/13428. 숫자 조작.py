T = int(input())

for t in range(T):
    N = int(input())
    
    strN = str(N)
    
    min_ = N
    max_ = N
    
    for i in range(len(strN)-1):
        for j in range(i+1, len(strN)):            
            convertN = list(strN)
            convertN[i], convertN[j] = convertN[j], convertN[i]
            
            if convertN[0] == '0': continue
                
            min_ = min(min_, int(''.join(convertN)))
            max_ = max(max_, int(''.join(convertN)))
    
    print(f'#{t+1} {min_} {max_}')