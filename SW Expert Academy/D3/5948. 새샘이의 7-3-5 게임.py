T = int(input())

for t in range(T):
    L = list(map(int, input().split()))
    L.sort()
    
    S = set()
    lenL = len(L)
    
    for i in range(lenL):
        for j in range(i+1, lenL):
            for k in range(j+1, lenL):
                S.add(sum([L[lenL-i-1], L[lenL-j-1], L[lenL-k-1]]))
    
    print(f'#{t+1} {list(sorted(S))[-5]}')