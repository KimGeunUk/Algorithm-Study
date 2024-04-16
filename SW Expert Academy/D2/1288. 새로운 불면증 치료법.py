T = int(input())

for i in range(T):
    N = int(input())
    N_set = set()      
    j = 1
    
    while len(N_set) != 10:
        M = N * j
        
        for n in str(M):
            N_set.add(int(n))
            
        j += 1
    
    print(f'#{i+1} {M}')