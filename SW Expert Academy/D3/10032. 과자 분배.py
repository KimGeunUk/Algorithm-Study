T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    
    div, mod = divmod(N, K)
    
    print(f'#{t+1} {mod}')