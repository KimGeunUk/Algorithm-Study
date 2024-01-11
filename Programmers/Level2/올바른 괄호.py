def solution(s):
    if s[0] == ")":
            return False

    idx = 0
    count = 0
    
    while idx < len(s):
        if s[idx] == ")":
            count -= 1
        else:
            count += 1
        
        idx += 1
        
        if count < 0:
            return False
    
    if count > 0:
        return False
    
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("())()(()"))