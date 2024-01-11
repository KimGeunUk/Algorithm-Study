import copy
def solution(picks, minerals):
    answer = []

    tired = [[1, 1, 1],
             [5, 1, 1],
             [25, 5, 1]]
    
    index = {'diamond': 0, 'iron': 1, 'stone': 2}
    
    def dfs(picks, minerals, value):
        if sum(picks) == 0 or minerals == []:
            answer.append(value)
        
        m = minerals[:5]
        
        can = []
        for idx, pick in enumerate(picks):
            if pick == 0: continue
            else: can.append(idx)

        for c in can:
            v = 0
            for m_ in m:
                v += tired[c][index[m_]]
            
            temp = copy.deepcopy(picks)
            temp[c] -= 1
            
            dfs(temp, minerals[5:], value + v)

    dfs(picks, minerals, 0)

    return min(answer)

def solution(picks, minerals):
    answer = 0
    
    minerals = minerals[:sum(picks)*5]
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    costs = []
    for mineral in minerals:
        cost = [0, 0, 0] # dia, iron, ston
        for mine in mineral:
            if mine == 'diamond':
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mine == 'iron':
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
    
    costs = sorted(costs, key=lambda x: (-x[0], -x[1], -x[2]))
    
    for cost in costs:
        if picks[0] > 0:
            picks[0] -= 1
            answer += cost[0]
            continue
        elif picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
            continue
        elif picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
            continue
    
    return answer
        

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) # 12
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) # 50
print(solution([1, 1, 0], ["stone", "stone", "iron", "stone", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]))