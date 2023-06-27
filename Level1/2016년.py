def solution(a, b):
    answer = ''
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    #1월 1일 = 금요일

    if a == 1:
        if b % 7 == 1:
            answer = day[5]
        elif b % 7 == 2:
            answer = day[6]
        elif b % 7 == 3:
            answer = day[0]
        elif b % 7 == 4:
            answer = day[1]
        elif b % 7 == 5:
            answer = day[2]
        elif b % 7 == 6:
            answer = day[3]
        elif b % 7 == 0:
            answer = day[4]
    elif a == 2:
        if b % 7 == 1:
            answer = day[1]
        elif b % 7 == 2:
            answer = day[2]
        elif b % 7 == 3:
            answer = day[3]
        elif b % 7 == 4:
            answer = day[4]
        elif b % 7 == 5:
            answer = day[5]
        elif b % 7 == 6:
            answer = day[6]
        elif b % 7 == 0:
            answer = day[0]
    elif a == 3:
        if b % 7 == 1:
            answer = day[2]
        elif b % 7 == 2:
            answer = day[3]
        elif b % 7 == 3:
            answer = day[4]
        elif b % 7 == 4:
            answer = day[5]
        elif b % 7 == 5:
            answer = day[6]
        elif b % 7 == 6:
            answer = day[0]
        elif b % 7 == 0:
            answer = day[1]
    elif a == 4:
        if b % 7 == 1:
            answer = day[5]
        elif b % 7 == 2:
            answer = day[6]
        elif b % 7 == 3:
            answer = day[0]
        elif b % 7 == 4:
            answer = day[1]
        elif b % 7 == 5:
            answer = day[2]
        elif b % 7 == 6:
            answer = day[3]
        elif b % 7 == 0:
            answer = day[4]
    elif a == 5:
        if b % 7 == 1:
            answer = day[0]
        elif b % 7 == 2:
            answer = day[1]
        elif b % 7 == 3:
            answer = day[2]
        elif b % 7 == 4:
            answer = day[3]
        elif b % 7 == 5:
            answer = day[4]
        elif b % 7 == 6:
            answer = day[5]
        elif b % 7 == 0:
            answer = day[6]
    elif a == 6:
        if b % 7 == 1:
            answer = day[3]
        elif b % 7 == 2:
            answer = day[4]
        elif b % 7 == 3:
            answer = day[5]
        elif b % 7 == 4:
            answer = day[6]
        elif b % 7 == 5:
            answer = day[0]
        elif b % 7 == 6:
            answer = day[1]
        elif b % 7 == 0:
            answer = day[2]
    elif a == 7:
        if b % 7 == 1:
            answer = day[5]
        elif b % 7 == 2:
            answer = day[6]
        elif b % 7 == 3:
            answer = day[0]
        elif b % 7 == 4:
            answer = day[1]
        elif b % 7 == 5:
            answer = day[2]
        elif b % 7 == 6:
            answer = day[3]
        elif b % 7 == 0:
            answer = day[4]
    elif a == 8:
        if b % 7 == 1:
            answer = day[1]
        elif b % 7 == 2:
            answer = day[2]
        elif b % 7 == 3:
            answer = day[3]
        elif b % 7 == 4:
            answer = day[4]
        elif b % 7 == 5:
            answer = day[5]
        elif b % 7 == 6:
            answer = day[6]
        elif b % 7 == 0:
            answer = day[0]
    elif a == 9:
        if b % 7 == 1:
            answer = day[4]
        elif b % 7 == 2:
            answer = day[5]
        elif b % 7 == 3:
            answer = day[6]
        elif b % 7 == 4:
            answer = day[0]
        elif b % 7 == 5:
            answer = day[1]
        elif b % 7 == 6:
            answer = day[2]
        elif b % 7 == 0:
            answer = day[3]
    elif a == 10:
        if b % 7 == 1:
            answer = day[6]
        elif b % 7 == 2:
            answer = day[0]
        elif b % 7 == 3:
            answer = day[1]
        elif b % 7 == 4:
            answer = day[2]
        elif b % 7 == 5:
            answer = day[3]
        elif b % 7 == 6:
            answer = day[4]
        elif b % 7 == 0:
            answer = day[5]
    elif a == 11:
        if b % 7 == 1:
            answer = day[2]
        elif b % 7 == 2:
            answer = day[3]
        elif b % 7 == 3:
            answer = day[4]
        elif b % 7 == 4:
            answer = day[5]
        elif b % 7 == 5:
            answer = day[6]
        elif b % 7 == 6:
            answer = day[0]
        elif b % 7 == 0:
            answer = day[1]
    elif a == 12:
        if b % 7 == 1:
            answer = day[4]
        elif b % 7 == 2:
            answer = day[5]
        elif b % 7 == 3:
            answer = day[6]
        elif b % 7 == 4:
            answer = day[0]
        elif b % 7 == 5:
            answer = day[1]
        elif b % 7 == 6:
            answer = day[2]
        elif b % 7 == 0:
            answer = day[3]

    return answer

print(solution(5,24))