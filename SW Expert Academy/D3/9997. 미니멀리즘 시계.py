T = int(input())

for t in range(T):
    theta = int(input())
    
    div, mod = divmod(theta * 2, 60)
    
    print(f'#{t+1} {div} {mod}')