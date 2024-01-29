def collatz(n):
    area = []    
    idx = 0
    
    while n > 1:
        pn = n
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        
        idx += 1

        area.append((n + pn)/2.0)
    
    return area
        

def solution(k, ranges):
    answer = []
    
    area = collatz(k)
    
    for range in ranges:
        a = range[0]
        b = (len(area) + 1) + range[1]
        
        if a < b:
            answer.append(sum(area[a:b-1]))
        else:
            answer.append(-1.0)

    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])) # [33.0,31.5,0.0,-1.0]
print(solution(3, [[0,0], [1,-2], [3,-3]])) # [47.0,36.0,12.0]