from collections import defaultdict
def solution(keymap, targets):
    answer = [-1 for _ in range(len(targets))]
    
    dd = defaultdict(lambda: 101)
    
    for key_ in keymap:
        for idx, k in enumerate(key_, start=1):
            dd[k] = min(dd[k], idx)
    
    for idx, target in enumerate(targets):
        for t in target:
            if t in dd.keys():
                answer[idx] += dd[t]
            else:
                answer[idx] = -1
                break
        else:
            answer[idx] += 1
    
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9, 4]
print(solution(["AA"], ["B"])) # [-1]
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"])) # [4, 6]
print(solution(["BC"], ["AC", "BC"])) # [-1]