import itertools

def euclidean(a, b, c, d):
    return abs(a-c) + abs(b-d)

def solution(places):
    answer = []
    
    p_list = []
    o_list = []
    x_list = []
    
    for place in places:
        for r, row in enumerate(place):
            for c, col in enumerate(row):
                if col == 'P':
                    p_list.append([r,c])
                elif col == 'O':
                    o_list.append([r,c])
                elif col == 'X':
                    x_list.append([r,c])        
    
        # 시간초과 확인
        p_iter = list(itertools.combinations(p_list, 2))
        
        for idx, p in enumerate(p_iter):
            euc = euclidean(p[0][0], p[0][1], p[1][0], p[1][1])
            now_answer = 1
            
            if euc <= 2:
                if p[0][0] != p[1][0] and p[0][1] != p[1][1]:
                    if [p[0][0],p[1][1]] in x_list and [p[1][0], p[0][1]] in x_list:
                        now_answer = 1
                    else:
                        answer.append(0)
                        now_answer = 0
                        break
                elif p[0][0] == p[1][0]:
                    if [p[0][0], (p[0][1]+p[1][1])//2] in x_list:
                        now_answer = 1
                    else:
                        answer.append(0)
                        now_answer = 0
                        break
                elif p[0][1] == p[1][1]:                    
                    if [(p[0][0]+p[1][0])//2, p[0][1]] in x_list:
                        now_answer = 1
                    else:
                        answer.append(0)
                        now_answer = 0
                        break  
                else:
                    answer.append(0)
                    now_answer = 0
                    break
            
                               
        if now_answer == 1:
            answer.append(1)
            
        p_list = []
        o_list = []
        x_list = []
        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

print(solution([["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]]))