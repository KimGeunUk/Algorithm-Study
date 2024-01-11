def sco(a, b):
    if a < b:
        return a + (b * 2)
    else:
        return b + (a * 2)

# 여러가지 방법을 사용해봤지만 전부 효율성 테스트에서 떨어졌다. heapq를 사용하여 풀어야 한다.
def solution_fail(scoville, K):
    answer = 0
    count = 0
    sorted_sco = sorted(scoville)
    j = 3
    while True:             
        if sorted_sco[0] < K:
            if len(sorted_sco) == 1:
                break
            
            sco_score = sco(sorted_sco[0], sorted_sco[1])
            
            if sco_score >= K:
                count += 1
                
            if len(sorted_sco) <= 3:
                sorted_sco = [sco_score] + sorted_sco[2:]
            elif len(sorted_sco) > 3:
                if sco_score <= sorted_sco[3]:
                    sorted_sco = [sorted_sco[2]] + [sco_score] + sorted_sco[3:]
                elif sco_score > sorted_sco[3]:                    
                    for i in range(3, len(sorted_sco)-1):                        
                        if sco_score <= sorted_sco[i]:
                            j = i
                            break
                        if sorted_sco[i] >= K or sco_score >= K:
                            break
                    sorted_sco = sorted_sco[2:j] + [sco_score] + sorted_sco[j:]
            answer += 1
        else:
            break
                    
    if answer == 0 or count == 0:
        return -1
    else: 
        return answer  

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer
    

print(solution([2, 3, 3, 7, 10, 12], 7))
print(solution([0, 2, 3, 1], 9))
print(solution([0, 0], 3))