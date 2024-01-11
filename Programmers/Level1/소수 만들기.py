def solution(nums):
    answer = 0

    sum = []

    count=0

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum.append(nums[i] + nums[j] + nums[k])
    
    sum.sort()
    
    for i in range(len(sum)):
        for j in range(2, sum[i]+1):
            if sum[i] % j == 0:
                count += 1
        
        if count == 1:
            answer += 1

        count = 0   

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))