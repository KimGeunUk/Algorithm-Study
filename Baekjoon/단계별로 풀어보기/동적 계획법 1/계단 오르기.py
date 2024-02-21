N = int(input()) # <= 300

stair = [int(input()) for _ in range(N)]

DP = [0] * N

if len(stair) <= 2:
    print(sum(stair))
else:
    DP[0] = stair[0]
    DP[1] = max(stair[0] + stair[1], stair[1]) # 한 칸 + 한 칸, 두 칸
    DP[2] = max(stair[0] + stair[2], stair[1] + stair[2]) # 한 칸 + 두 칸 or 두 칸 + 한 칸

    for i in range(3, N):
        DP[i] = max(DP[i-2]+stair[i], DP[i-3]+stair[i-1]+stair[i])

    print(DP.pop())