from itertools import combinations as c

def solution(weights):
    answer = 0
    weights = sorted(weights)

    ratios = [1/1, 1/2, 2/3, 3/4]
    
    for w in list(c(weights, 2)):
        a, b = w
        
        if a/b in ratios:
            answer+=1

    return answer

from collections import defaultdict
def solution(weights):
    answer = 0

    weights_dict = defaultdict(float)
    ratio = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3]
    
    for w in weights:
        for r in ratio:
            answer += weights_dict[r * w]
        weights_dict[w] += 1

    return int(answer)

print(solution([100,180,360,100,270])) # 4