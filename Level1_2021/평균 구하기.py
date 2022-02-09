def solution(arr):
    answer = 0

    sum = 0

    for i in arr:
        sum += int(i)

    sum = sum / len(arr)

    answer = sum
    
    return answer

print(solution([1,2,3,4]))
print(solution([5,5]))