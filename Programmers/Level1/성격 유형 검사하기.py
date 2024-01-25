def solution(survey, choices):
    answer = ''
    
    point = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for s, c in zip(survey, choices):
        if c < 4: # 1 2 3
            point[s[0]] += abs(c - 4)
        elif c > 4: # 5 6 7
            point[s[1]] += abs(c - 4)

    
    groups = ['RT', 'CF', 'JM', 'AN']
    
    for group in groups:
        if point[group[0]] >= point[group[1]]:
            answer += group[0]
        elif point[group[0]] < point[group[1]]:
            answer += group[1]
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # RCJA