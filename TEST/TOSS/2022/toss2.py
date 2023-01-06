def DFS(load, M, depth):
    box_list = list()
    
    if depth < len(load):
        if sum(load[depth:]) <= M:
            return box_list.append(sum(load[depth]))
    else:
        DFS(load, M, depth+1)
        return box_list

def solution(M, load):
    global answer
    answer = list()
    
    DFS(load, M, 1)

    return answer


print(solution(10, [2,3,7,8]))
# print(solution(5, [2,2,2,2,2]))
# print(solution(16,15,9,17,1,3))