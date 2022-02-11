def solution(numbers, hand):
    answer = ''

    current_Lhand = '*'
    current_Rhand = '#'
    L_dis = None
    R_dis = None
    
    dis_2 = {0:[2], 1:[1,3,5], 2:[4,8,6], 3:[0,7,9], 4:['*','#']}
    dis_5 = {0:[5], 1:[2,4,6,8], 2:[0,1,3,7,9], 3:['*','#']}
    dis_8 = {0:[], 1:[0,5,7,9], 2:['*', '#', 4, 6, 2], 3:[1, 3]}
    dis_0 = {0:[0], 1:['*', '#', 8], 2:[5,7,9], 3:[2,4,6], 4:[1,3]}
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            current_Lhand = i
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            current_Rhand = i
        else:
            if i == 2:
                for k, v in dis_2.items():
                    if current_Lhand in v:
                        L_dis = k
                    if current_Rhand in v:
                        R_dis = k
                if L_dis < R_dis:
                    answer += "L"
                    current_Lhand = i
                elif L_dis > R_dis:
                    answer += "R"
                    current_Rhand = i
                elif L_dis == R_dis:
                    if hand == "left":
                        answer += "L"
                        current_Lhand = i
                    elif hand == "right":
                        answer += "R"
                        current_Rhand = i
            elif i == 5:
                for k, v in dis_5.items():
                    if current_Lhand in v:
                        L_dis = k
                    if current_Rhand in v:
                        R_dis = k
                if L_dis < R_dis:
                    answer += "L"
                    current_Lhand = i
                elif L_dis > R_dis:
                    answer += "R"
                    current_Rhand = i
                elif L_dis == R_dis:
                    if hand == "left":
                        answer += "L"
                        current_Lhand = i
                    elif hand == "right":
                        answer += "R"
                        current_Rhand = i
            elif i == 8:
                for k, v in dis_8.items():
                    if current_Lhand in v:
                        L_dis = k
                    if current_Rhand in v:
                        R_dis = k
                if L_dis < R_dis:
                    answer += "L"
                    current_Lhand = i
                elif L_dis > R_dis:
                    answer += "R"
                    current_Rhand = i
                elif L_dis == R_dis:
                    if hand == "left":
                        answer += "L"
                        current_Lhand = i
                    elif hand == "right":
                        answer += "R"
                        current_Rhand = i
            elif i == 0:
                for k, v in dis_0.items():
                    if current_Lhand in v:
                        L_dis = k
                    if current_Rhand in v:
                        R_dis = k
                if L_dis < R_dis:
                    answer += "L"
                    current_Lhand = i
                elif L_dis > R_dis:
                    answer += "R"
                    current_Rhand = i
                elif L_dis == R_dis:
                    if hand == "left":
                        answer += "L"
                        current_Lhand = i
                    elif hand == "right":
                        answer += "R"
                        current_Rhand = i                  
    
    return answer

# 같은 번호를 두번 눌렀을 때의 경우의 수를 생각해야 한다. -> 이것떄문에 30분은 날린듯..

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
print(solution([2, 8, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

# Other Solution
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer