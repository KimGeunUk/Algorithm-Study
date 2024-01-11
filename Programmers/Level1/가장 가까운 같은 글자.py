from collections import defaultdict

def solution(s):
    answer = []
    
    d = defaultdict(lambda: -1)
    
    for idx, s_ in enumerate(s):
        if d[s_] == -1:
            answer.append(-1)
            d[s_] = idx
        else:
            answer.append(idx-d[s_])
            d[s_] = idx
    
    return answer

print(solution("banana"))
print(solution("foobar"))