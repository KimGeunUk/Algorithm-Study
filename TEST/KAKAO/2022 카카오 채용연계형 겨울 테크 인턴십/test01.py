from copy import deepcopy

def dfs(x, y, z, visited, answer):    
    z -= 1
    visited.append(x)
    print(x, y, z, visited)
    
    if z == 0:
        if x == y:
            answer.append(max(visited))
            
    new_visited = deepcopy(visited)
    
    if abs(x-y) < z:
        dfs(x+1, y, z, new_visited, answer)
        dfs(x-1, y, z, new_visited, answer)
        
    elif abs(x-y) == z:
        if x < y:
            dfs(x+1, y, z, new_visited, answer)
        elif x > y:
            dfs(x-1, y, z, new_visited, answer)
    else:
        return 
            
def solution(x, y, z):
    answer = []  
    visited = [x]
    
    if x <= y:
        dfs(x+1, y, z, visited, answer)
    elif x > y:
        dfs(x-1, y, z, visited, answer)

    if len(answer) == 0:
        return -1
    else:
        return max(answer)

print(solution(8, 5, 3))
print(solution(4, 4, 6))
print(solution(5, 5, 4))