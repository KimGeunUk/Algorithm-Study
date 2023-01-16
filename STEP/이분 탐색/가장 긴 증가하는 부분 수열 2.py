import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

LIS = [nums[0]]

for num in nums:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        start = 0
        end = len(LIS)-1        
        while start <= end:
            mid = (start+end)//2
            
            if LIS[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        
        LIS[start] = num
        
print(len(LIS))