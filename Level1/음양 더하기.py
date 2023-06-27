def solution(absolutes, signs):
    answer = 0
    
    for i, j in zip(absolutes, signs):
        if j == True:
            i = +i
        else:
            i = -i
        answer += i
    
    return answer

print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))