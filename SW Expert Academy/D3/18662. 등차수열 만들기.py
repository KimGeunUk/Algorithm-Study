T = int(input())

for i in range(T):
    x, y, z = map(int, input().split())
    
    if y - x == z - y: print(f'#{i+1} 0.0')
    else:
        a = abs((y - (z - y)) - x)        
        b = abs((x + ((z - x) / 2)) - y)        
        c = abs((y + (y - x)) - z)
        
        print(f'#{i+1} {min(a, b, c):.1f}')