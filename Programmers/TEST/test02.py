def solution(places):
    answer = []
    p = []
    x = []
    sum = 0

    Q = 0
    while Q < len(places):
        for i in range(len(places[Q])):
            for j in range(len(places[Q][0])):
                if places[Q][i][j] == 'P':
                    p.append([i,j])
                elif places[Q][i][j] == 'X':
                    x.append([i,j])

        for i in range(len(p)-1):
            for j in range(i+1, len(p)):
                if abs(p[i][0]-p[j][0]) + abs(p[i][1]-p[j][1]) > 2:
                    sum += 0
                else:
                    # 거리 2이하인데 한 라인에서 일어나는 경우
                    if p[i][0] == p[j][0]:
                        if [p[i][0], (p[i][1]+p[j][1])/2] in x:
                            sum += 0
                        else:
                            sum += 1
                    elif p[i][1] == p[j][1]:
                        if [(p[i][0]+p[j][0])/2, p[i][1]] in x:
                            sum += 0
                        else:
                            sum += 1
                    # 거리 2이하이고 한 라인에서 일어나지 않은 경우
                    elif p[i][0] != p[j][0] and p[i][1] != p[j][1]:
                        if ([p[i][0], p[i][1]-1] in x and [p[j][0], p[j][1]+1] in x) or ([p[i][0], p[i][1]+1] in x and [p[j][0], p[j][1]-1] in x):
                            sum += 0
                        else:
                            sum += 1
                    # 거리가 1이하인 경우
                    elif abs(p[i][0]-p[j][0]) + abs(p[i][1]-p[j][1]) == 1 and abs(p[i][0]-p[j][0]) + abs(p[i][1]-p[j][1]) == 0:
                        sum += 1

        if sum == 0:
            answer.append(1)
        else:
            answer.append(0)

        Q += 1
        sum = 0
        p = []
        x = []

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))