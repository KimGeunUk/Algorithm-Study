def solution(skills, team, k):
    dic_skill_team = {skills[i]:i+1 for i in range(len(skills))}
    
    skill_list = list()
    team_list = list()
    team_k = list()
    
    for i in range(len(skills)-k+1):
        skill_list.append(skills[i:i+k])
        team_list.append([i+1 for i in range(i,i+k)])
    
    skill_sum_list = list()
    
    best = 0
    for i, j in zip(skill_list, team_list):        
        count = 0
        
        if len(team) == len(skills):
            count == len(team)
        else:
            for k in team:
                if k in j:
                    count +=1
        
        sum_a = 0
        if count == len(team):
            sum_a += sum(i)*2
        else:
            sum_a += sum(i)
            
        if sum_a > best:
            best = sum_a
            
    return best

print(solution([3, 2, 4, 1], [2, 4], 3))
print(solution([1, 1, 4, 2, 1, 1], [2, 1, 5], 4))
print(solution([5, 8, 3, 1], [4, 3], 2))
print(solution([2], [1], 1))
