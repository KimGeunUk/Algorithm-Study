import re

def solution(record):
    answer = []
    new = []
    id_nic = dict()

    for i in record:
        j = i.split(' ')
        if j[0] == 'Enter':
            id_nic[j[1]] = j[2]
            answer.append(j[1] + '님이 들어왔습니다.')
        elif j[0] == 'Leave':
            answer.append(j[1] + '님이 나갔습니다.')
        elif j[0] == 'Change':
            id_nic[j[1]] = j[2]
    print(answer)
    for i in answer:
        new.append(re.sub(i.split('님')[0], id_nic[i.split('님')[0]], i))

    return new

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))