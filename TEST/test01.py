from collections import Counter as ct

def solution(s):
    answer = ''
    tos = ''
    tos_answer = ''
    
    s = s.lower()
    a = ct(s)
    
    m = list(a.most_common())[0][1]
    for i in a.items():        
        if i[1] == m:
            if i[0] == 't' or i[0] == 'o' or i[0] == 's':
                tos += i[0]
            else:
                answer += i[0]
                        
    if 't' in tos:
        tos_answer += 'T'
    if 'o' in tos:
        tos_answer += 'O'
    if 's' in tos:
        tos_answer += 'SS'
    
    answer = sorted(list(answer))
    answer = ''.join(answer)
    
    return tos_answer + answer

print(solution("baaaabbbssdd"))
print(solution("sqotdsdryetvtutsoowdeodevvsve"))
print(solution("BA"))
# print(solution("BbA"))
# print(solution("aaBBTtooSS"))