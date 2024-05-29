import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

sum_arr = sum(arr)
max_arr = max(arr)

if sum_arr <= M:
    print(max_arr)
else:
    start = 0
    end = max_arr
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        sum_ = sum(min(mid, j) for j in arr)
        
        if sum_ <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(result)
