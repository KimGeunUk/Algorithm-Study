from collections import Counter

def solution(X, Y):
    answer = []
    
    XC = Counter(X)
    YC = Counter(Y)
    
    for key in set(XC.keys()) & set(YC.keys()):
        n = min(XC[key], YC[key])
        for _ in range(n):
            answer.append(key)
    
    answer.sort(reverse=True)
    answer = ''.join(answer)
    
    if answer == '':
        return "-1"
    elif set(answer) == {"0"}:
        return "0"
    else:
        return answer


print(solution("100", "2345")) # -1
print(solution("100", "203045")) # 0
print(solution("100", "123450")) # 10
print(solution("12321", "42531")) # 321
print(solution("5525", "1255")) # 552