T = int(input())

for i in range(T):
    a, b = map(int, input().split())

    if a == b: print(f'#{i+1} {a}')
    else: print(f'#{i+1} 1')