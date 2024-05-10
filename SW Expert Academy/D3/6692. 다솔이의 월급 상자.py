T = int(input())

for t in range(T):
    N = int(input())
    
    answer = 0
    
    for _ in range(N):
        p, x = map(float, input().split())
        
        answer += p * x
        
    print(f'#{t+1} {answer:.6f}')