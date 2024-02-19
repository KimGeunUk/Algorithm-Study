from itertools import product

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
    answer = set()

    result = [[] for _ in range(len(banned_id))]
    
    for i in range(len(banned_id)):
        for u in user_id:
            if ismatch(banned_id[i], u):
                result[i].append(u)

    print(result)
    
    result = list(map(set, product(*result)))
    
    for r in result:
        if len(r) == len(banned_id):
            answer.add(tuple(sorted(r)))

    return len(answer)


def solution(user_id, banned_id):
    answer = set()
        
    def bfs(b_idx, visited, user_id_list):
        nonlocal answer
        
        if b_idx == len(banned_id):
            answer.add(tuple(sorted(user_id_list)))
            return
        
        for u_idx in range(len(user_id)):                         
            if visited[u_idx] == False:
                if ismatch(user_id[u_idx], banned_id[b_idx]):
                    
                    visited[u_idx] = True                    
                    user_id_list.append(user_id[u_idx])

                    bfs(b_idx+1, visited, user_id_list)
                    
                    if b_idx == 0:
                        user_id_list = []
                    else:
                        user_id_list = user_id_list[:b_idx]
                    visited[u_idx] = False
                    
    
    visited = [False for _ in range(len(user_id))]
    
    bfs(0, visited, [])
    
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3