T = int(input())

for t in range(T):
    S = input().strip()
    
    D = dict()
    for s in S:
        if s in D.keys():
            D[s] += 1
        else:
            D[s] = 1
            
    if len(D.keys()) != 2:
        print(f'#{t+1} No')
    elif D[S[0]] != 2:
        print(f'#{t+1} No')
    else:
        print(f'#{t+1} Yes')