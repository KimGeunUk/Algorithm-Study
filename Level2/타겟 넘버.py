def solution(numbers, target):
    answer = 0

    sum = 0
    i = 0
    plus_list = []
    minus_list = []
    
    while sum != target:
        if sum <= target:
            sum += numbers[i]
            plus_list.append((i, numbers[i]))
        else:
            sum -= numbers[i]
            minus_list.append((i, numbers[i]))
        i += 1
    
    print(plus_list)
    print(minus_list)



print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4))    # 2
print(solution([1, 2, 1, 2], 2))    # 3
print(solution([1, 2, 1, 2], 6))    # 1