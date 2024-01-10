from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    
    heap = []
    
    for idx, e in enumerate(enemy):
        if len(heap) < k:
            heappush(heap, e)
        else:
            if n > 0:
                n -= heappop(heap)
        
        

    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))