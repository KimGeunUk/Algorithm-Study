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
    
    print(min_, max_)
    
    # numbers = list(map(int, strN))
    # min_, max_ = min(numbers), max(numbers)
   
    # min_index, max_index = strN.index(str(min_)), strN.index(str(max_))
    # strN[min_index], strN[max_index] = strN[max_index], strN[min_index]
    # max_N = ''.join(strN)
     
    # print(f'#{t+1} {N} {max_N}')