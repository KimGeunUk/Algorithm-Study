T = int(input())

for t in range(T):
    n, d = map(int, input().split())
    
    d = 1 + 2 * d
    
    div, mod = divmod(n, d)
    
    if mod > 0: div += 1
    
    print(f'#{t+1} {div}')