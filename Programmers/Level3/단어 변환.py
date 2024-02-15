from collections import deque

def ischangable(a, b):
    count = 0
    
    for _a, _b in zip(a, b):
        if _a == _b:
            count += 1
    
    if count == len(a)-1:
        return True
    else:
        return False

def bfs(i, words, visited, target):
    visited[i] = True
    
    q = deque()
    q.append([i, 0])

    while q:
        pop = q.popleft()
        visited[pop[0]] = True

        for j in range(len(words)):
            if visited[j] == False:
                if ischangable(words[pop[0]], words[j]):
                    q.append([j, pop[1]+1])

                    if words[j] == target:
                        return pop[1] + 1
                

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False for _ in range(len(words)+1)]
    
    words = [begin] + words
    
    return bfs(0, words, visited, target)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"])) # 4