T = int(input())

for t in range(T):
    K = int(input())
    
    L = []
    count = 0
    for _ in range(K):
        n = int(input())
        if n == 0:
            L.pop()
        else:
            count += 1
            L.append(n)
    
    print(f'#{t+1} {sum(L)}')