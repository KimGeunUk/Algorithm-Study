def solution(n, m):
    line = '' 
    for i in range(m):
        line += '*'*n
        line += '\n'
    
    return line
    
print(solution(5, 3))