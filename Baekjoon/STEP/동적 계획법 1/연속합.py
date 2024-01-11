import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

DP = [0] * N
DP[0] = nums[0]
for i in range(1, N):
    DP[i] = max(nums[i], DP[i-1]+nums[i])
print(max(DP))

# 시간 초과
# DP = [0] * N
# max_ = -float('inf')

# DP[0] = nums[0]
# max_ = max(DP[0], max_)

# for n in range(1, N):    
#     for idx in range(n):
#         DP[idx] = DP[idx] + nums[n] 
#         max_ = max(DP[idx], max_)

#     DP[n] = nums[n]
#     max_ = max(DP[n], max_)
    
# print(max_)


