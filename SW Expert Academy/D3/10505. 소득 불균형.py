T = int(input())

for t in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    avg = int(sum(L) / len(L))
    count = 0
    for l in L:
        if l <= avg: count += 1
        
    print(f'#{t+1} {count}')