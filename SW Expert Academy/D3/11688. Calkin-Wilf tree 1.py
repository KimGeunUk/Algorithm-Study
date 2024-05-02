T = int(input())

for t in range(T):
    S = input().strip()
    
    a, b = 1, 1
    
    for s in S:
        if s == 'L':
            a, b = a, a + b
        elif s == 'R':
            a, b = a + b, b
    
    print(f'#{t+1} {a} {b}')