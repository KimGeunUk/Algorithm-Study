import sys
input = sys.stdin.readline

N = int(input())

count = 0

for _ in range(N):
    word = input().strip()
    
    stack = []
    
    for w in word:
        if not stack:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    
    if not stack:
        count += 1
        
print(count)