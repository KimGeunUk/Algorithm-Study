import sys
input = sys.stdin.readline

from collections import Counter

TC = int(input())

for _ in range(TC):
    N = int(input())    
    teams = list(map(int, input().split()))
    
    qualified_teams = []
    for key, value in Counter(teams).items():
        if value >= 6:
            qualified_teams.append(key)
    
    scores = [team for team in teams if team in qualified_teams]
    counter = {}
    for idx, score in enumerate(scores, start=1):
        if score not in counter.keys():
            counter[score] = [idx, [idx]]
        else:
            counter[score][1].append(idx)
            if len(counter[score][1]) < 5:
                counter[score][0] += idx

    winner = None
    min_sum_score = min([counter[key][0] for key in counter.keys()])    
    min_5_score = 1001    
    for key, value in counter.items():
        if value[0] == min_sum_score:
            if min_5_score > value[1][4]:                
                winner = key
                min_5_score = value[1][4]
            
    print(winner)