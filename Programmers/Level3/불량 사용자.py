from collections import Counter

def ismatch(a, b):
    if len(a) != len(b):
        return False
    
    for _a, _b in zip(a, b):
        if _a == '*' or _b == '*':
            continue
        elif _a == _b:
            continue
        else:
            return False
    else:
        return True

def solution(user_id, banned_id):
    answer = 1
    
    c = Counter(banned_id)
    for k, v in c.items():
        if v > 1:
            for ui in user_id:
                if ismatch(k, ui):
                    for _ in range(v-1):
                        user_id.remove(ui)
                    for _ in range(v-1):
                        banned_id.remove(k)
                    break
                
    
    b = [[] for _ in range(len(banned_id))]
    count = 0
    for idx, bi in enumerate(banned_id):
        for ui in user_id:
            if ismatch(bi, ui):
                if idx > 0:
                    for _b in b[:idx]:
                        if ui in _b:
                            count += 1
                b[idx].append(ui)

    for _b in b:
        answer *= len(_b)
        
    return answer - count

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3