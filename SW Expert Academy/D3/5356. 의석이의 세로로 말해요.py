T = int(input())

for t in range(T):
    L = [list(input().strip()) for _ in range(5)]

    lenL = []
    for l in L:
        lenL.append(len(l))
    
    maxL = max(lenL)
    for idx, l in enumerate(L):
        for i in range(maxL-len(l)):
            L[idx].append('')
            
    L = list(map(list, zip(*L)))
    
    print(f'#{t+1}', end=' ')
    for l in L:
        print(''.join(l), end='')
    print()
