def solution(sticker):
    L = len(sticker)
    
    if L == 1: return sticker[0]
    
    DP1 = [0] * L
    DP1[0], DP1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, (L - 1)):
        DP1[i] = max(DP1[i - 1], DP1[i - 2] + sticker[i])
        
    DP2 = [0] * L
    DP2[0], DP2[1] = 0, sticker[1]
    for i in range(2, L):
        DP2[i] = max(DP2[i - 1], DP2[i - 2] + sticker[i])

    return max(max(DP1), max(DP2))

print(solution([14, 6, 5, 11, 3, 9, 2, 10])) # 36
print(solution([1, 3, 2, 5, 4])) # 8