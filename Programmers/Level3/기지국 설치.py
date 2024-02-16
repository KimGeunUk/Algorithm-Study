def solution(n, stations, w):
    answer = 0
    
    before = 0
    
    for station in stations:
        start, end = station - w, station + w
        
        if start < 0: start = 0
        if end > n: end = n
        
        cnt = start - before - 1
        if cnt > 0:
            if cnt % (1+w*2) == 0:
                answer += int(cnt/(1+w*2))
            else:
                answer += int(cnt/(1+w*2)) + 1
            
        before = end
    else:
        if end != n:
            cnt = n - before
            if cnt % (1+w*2) == 0:
                answer += int(cnt/(1+w*2))
            else:
                answer += int(cnt/(1+w*2)) + 1


    return answer

print(solution(11, [4, 11], 1)) # 3
print(solution(16, [9], 2)) # 3
print(solution(6, [4], 2)) # 2