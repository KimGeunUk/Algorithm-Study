T = int(input())

for t in range(T):
    N = int(input())
    
    r = round(N, -len(str(N))+2)
    
    print(f'#{t+1} {r / 10**(len(str(r))-1)}*10^{len(str(r))-1}')