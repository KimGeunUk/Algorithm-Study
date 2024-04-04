T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    
    d, m = divmod(a, b)
    
    print(f'#{i} {d} {m}')