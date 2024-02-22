from collections import deque

def solution(stones, k):
    answer = float('inf')
    q = deque()    

    for idx, stone in enumerate(stones):
        while q and stones[q[-1]] < stone:
            q.pop()      
        q.append(idx)
        
        # 범위 조절
        if q[0] == idx - k:
            q.popleft()
        
        # 현재 idx 까지의 최대값들 중 최소값
        if idx >= k - 1:
            answer = min(answer, stones[q[0]])

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3
print(solution([7, 2, 8, 7, 2, 5, 9], 3)) # 7