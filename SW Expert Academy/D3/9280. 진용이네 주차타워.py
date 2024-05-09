T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    
    R = [int(input()) for _ in range(n)]
    W = [int(input()) for _ in range(m)]
    infos = [int(input()) for _ in range(2 * m)]
    
    parks = [None for _ in range(n)]
    waits = []
    
    count = 0
    
    for info in infos:
        if info >= 0:
            if None not in parks:
                waits.append(info)
            else:
                for i, park in enumerate(parks):
                    if park == None:
                        parks[i] = info
                        break
        else:
            for i, park in enumerate(parks):
                if park == (-info):                    
                    count += R[i] * W[(-info) - 1]
                    parks[i] = None
                    
                    if waits:
                        parks[i] = waits[0]
                        waits = waits[1:]
                    
                    break
    
    print(f'#{t+1} {count}')