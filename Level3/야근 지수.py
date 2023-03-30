import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    # 야근을 한 시점에서 남은 일의 작업량을 제곱하여 더한 값
    while n != 0:
        p = heapq.heappop(works)
        p += 1
        n -= 1        
        heapq.heappush(works, p)
    
    for work in works:
        answer += work * work
    
    return answer

print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1,1])) # 0