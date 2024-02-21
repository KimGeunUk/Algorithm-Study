N = int(input())
nums = list(map(int, input().split()))

DP = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            DP[i] = max(DP[i], DP[j] + 1)

for i in range(N):
    for j in range(i):
        if nums[i] < nums[j]:
            DP[i] = max(DP[i], DP[j] + 1)
        
print(max(DP))
