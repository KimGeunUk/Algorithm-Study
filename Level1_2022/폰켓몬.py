def solution(nums):
    answer = 0
    
    get = len(nums)//2
    num = set(nums)
    
    answer = min(len(num),get)
    
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))

# 이게 맞나 ?

def solution(ls):
    return min(len(ls)/2, len(set(ls)))

# 맞는 것 같다.