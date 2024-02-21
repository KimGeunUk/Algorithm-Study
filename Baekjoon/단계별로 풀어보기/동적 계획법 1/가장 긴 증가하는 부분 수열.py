N = int(input())
nums = list(map(int, input().split())) # 10 30 20 30 40 50

DP = [0] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and DP[i] < DP[j]:
            DP[i] = DP[j]
        
    DP[i] += 1

# DP = [1] * N
# 
# for i in range(N):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             DP[i] = max(DP[i], DP[j] + 1)
            
print(max(DP))