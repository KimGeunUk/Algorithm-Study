N = int(input())

wines = [int(input()) for _ in range(N)]

DP = [0] * N

if len(wines) <= 2:
    print(sum(wines))
elif len(wines) == 3:
    print(max(wines[0] + wines[1], wines[1] + wines[2], wines[0] + wines[2]))
else:
    DP[0] = wines[0]
    DP[1] = wines[0] + wines[1]
    DP[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
    DP[3] = max(DP[0] + wines[2] + wines[3], DP[1] + wines[3], DP[2])
    
    for i in range(4, N):
        DP[i] = max(DP[i-3] + wines[i-1] + wines[i], DP[i-2] + wines[i], DP[i-1])

    print(DP.pop())