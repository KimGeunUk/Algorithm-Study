import sys
input = sys.stdin.readline

brakets = input().strip()

stack = []
temp = 1
result = 0
for i, braket in enumerate(brakets):
    
    if braket == "(":
        temp *= 2
        stack.append("(")
    elif braket == "[":
        temp *= 3
        stack.append("[")
        
    elif braket == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        
        if brakets[i-1] == "(":
            result += temp
        
        temp //= 2
        stack.pop()

    elif braket == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        
        if brakets[i-1] == "[":
            result += temp
        
        temp //= 3
        stack.pop()

if stack:
    result = 0

print(result)