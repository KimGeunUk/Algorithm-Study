T = int(input())

for t in range(T):
    N = int(input())
    
    visited = []    
    count = 0
    
    for _ in range(N):
        Ai, Aj = map(int, input().split())
        
        if visited:
            for visit in visited:
                Bi, Bj = visit
                
                if Ai > Bi and Aj < Bj: count += 1
                elif Ai < Bi and Aj > Bj: count += 1
                
        visited.append((Ai, Aj))
    
    print(f'#{t+1} {count}')
