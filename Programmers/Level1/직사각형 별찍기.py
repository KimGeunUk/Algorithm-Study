def solution(n, m):
    line = '' 
    for i in range(m):
        line += '*'*n
        line += '\n'
    return line
    
print(solution(5, 3))

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*", end="")
    print(end='\n')

#print(a + b)