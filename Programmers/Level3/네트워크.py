from collections import deque
   
def solution(n, computers):
    def bfs(i, computers, n):
        visited[i] = True
        
        q = deque()
        q.append(i)
        
        while q:
            pop = q.popleft()
            visited[pop] = True
            
            for j in range(n):
                if computers[pop][j] == 1:
                    if visited[j] == False:
                        q.append(j)

    answer = 0
    visited = [False for _ in range(n)]    
    
    for i in range(n):
        if visited[i] == False:
            bfs(i, computers, n)
            answer += 1
    
    return answer

print(solution(3, [[1, 1, 0], 
                   [1, 1, 0],
                   [0, 0, 1]])) # 2

print(solution(3, [[1, 1, 0], 
                   [1, 1, 1], 
                   [0, 1, 1]])) # 1

print(solution(4, [[1, 1, 1, 0], 
                   [1, 1, 1, 0], 
                   [1, 1, 1, 0],
                   [0, 0, 0, 1]])) # 2

print(solution(6, [[1, 0, 0, 0, 0, 0], 
                   [1, 1, 0, 0, 0, 0], 
                   [1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 1, 0],
                   [0, 0, 0, 0, 1, 1]])) # 2

print(solution(7, [[1, 0, 0, 0, 0, 0, 1], 
                   [0, 1, 1, 0, 1, 0, 0], 
                   [0, 1, 1, 1, 0, 0, 0], 
                   [0, 0, 1, 1, 0, 0, 0], 
                   [0, 1, 0, 0, 1, 1, 0], 
                   [0, 0, 0, 0, 1, 1, 1], 
                   [1, 0, 0, 0, 0, 1, 1]])) # 1