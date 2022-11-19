from itertools import combinations as cb

def dfs(A, start):
    global team_list
    
    if len(A) == int(N/2):
        team_list.append([*A])
        return
    
    for idx in range(start, N):
        if idx not in A:
            A.append(idx)
            dfs(A, idx+1)
            A.pop()      
            
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

team_list = list()

min_ = float('inf')

dfs([], 0)

for (A, B) in zip(team_list[:int(len(team_list)/2)], team_list[::-1]):
 
    A_score = 0
    B_score= 0
    
    for (CA, CB) in zip(list(cb(A, 2)), list(cb(B, 2))):
        A_score += L[CA[0]][CA[1]] + L[CA[1]][CA[0]]
        B_score += L[CB[0]][CB[1]] + L[CB[1]][CB[0]]

    score = abs(A_score - B_score)
    min_ = min(score, min_)

print(min_)