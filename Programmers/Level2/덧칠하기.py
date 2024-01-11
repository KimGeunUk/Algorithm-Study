def solution(n, m, section):    
    answer = 1    
    paint_start = section[0]

    for sec in section[1:]:
        if sec < paint_start + m:
            pass
        else:
            paint_start = sec
            answer += 1
   
    return answer

print(solution(8, 4, [2, 3, 6])) # 2
print(solution(5, 4, [1, 3])) # 1
print(solution(4, 1, [1, 2, 3, 4])) # 4 