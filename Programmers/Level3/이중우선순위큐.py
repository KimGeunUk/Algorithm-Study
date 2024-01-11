import heapq
def solution(operations):
    answer = []
    
    h = []
    
    for oper in operations:
        order, index = oper.split(' ')        
        index = int(index)
        
        if order == 'I':
            heapq.heappush(h, index)
        else:
            if h:
                if index == 1:
                    h.remove(max(h))
                elif index == -1:
                    heapq.heappop(h)
    if h:
        answer.append(max(h))
        answer.append(heapq.heappop(h))
    else:
        answer = [0, 0]
    
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]