def solution(s):
    answer = True

    for i in s:
        if i.isalpha() == True:
            return False            
    
    if len(s) == 4 or len(s) == 6:
        answer = True
    else:
        answer = False

    return answer

print(solution('a234'))
print(solution('1234'))