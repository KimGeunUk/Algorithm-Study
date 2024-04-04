T = int(input())

for i in range(1, T + 1):
    N = int(input())
    
    previous = [1]
    
    print('1')
    
    for j in range(2, N + 1):
        
        new = []
        
        for k in range(j):
            if k - 1 < 0:
                new.append(previous[k])
            elif k > len(previous) - 1:
                new.append(previous[k - 1])
            else:
                new.append(previous[k - 1] + previous[k])
        
        previous = new
        
        print(' '.join(map(str, new)))
            
        
        