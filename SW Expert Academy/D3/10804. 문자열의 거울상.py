T = int(input())

for t in range(T):
    S = input().strip()
    
    print(f'#{t+1} ', end='')
    for s in S[::-1]:
        if s == 'b': print('d', end='')
        elif s == 'd': print('b', end='')
        elif s == 'p': print('q', end='')
        elif s == 'q': print('p', end='')
    print()