T = int(input())

for t in range(T):
    S = input().strip()
    
    A = None
    B = None
    
    if 1 <= int(S[:2]) <= 12:
        A = 'BOTH'
    else:
        A = 'YEAR'
    
    if 1 <= int(S[2:]) <= 12:
        B = 'BOTH'
    else:
        B = 'YEAR'
    
    if A == 'BOTH' and B == 'BOTH':
        print(f'#{t+1} AMBIGUOUS')
    elif A == 'YEAR' and B == 'BOTH':
        print(f'#{t+1} YYMM')
    elif A == 'BOTH' and B == 'YEAR':
        print(f'#{t+1} MMYY')
    else:
        print(f'#{t+1} NA')