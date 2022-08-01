# 다른 언어
def solution(str1):
    answer = ''
    for i in range(26):
        answer += chr(i+65)
    
    if str1 == 0:
        answer = answer.lower()
    else:
        answer = answer.upper()
    
    return answer

# string
import string
def solution(str1):    
    if str1 == 0:
        answer = string.ascii_lowercase
    else:
        answer = string.ascii_uppercase
    
    #모두
    answer = string.ascii_letters
    
    #숫자
    answer = string.digits
    return answer

print(solution(0))