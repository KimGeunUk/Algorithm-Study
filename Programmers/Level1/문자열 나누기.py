from collections import defaultdict

def solution(s):
    answer = 0
    
    start = None
    dd = defaultdict(int)
    
    for s_ in s:
        if start == None:
            start = s_
        
        if start == s_:
            dd[s_] += 1
        else:
            dd['other'] += 1
        
        if dd[start] == dd['other']:
            answer += 1
            start = None
            dd.clear()
    
    if dd[start] != dd['other']:
        answer += 1
    
    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
print(solution("xxxxxoooooxox")) # 3