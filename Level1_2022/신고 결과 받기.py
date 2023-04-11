# 2022 KAKAO

def solution(id_list, report, k):
    answer = []
    
    # id 와 신고를 당한 횟수 dic
    id_dic = {}
    # id 와 신고를 한 대상 dic
    report_dic = {}
    # 신고로 인해 정지 당한 대상 list
    out_list = []
    
    # init
    for id in id_list:
        id_dic[id] = 0
        report_dic[id] = []
    for r in report:
        print(r)
    
    # 이전에 같은 대상을 신고 하였으면 No count
    for id in report:
        if id.split(' ')[1] in report_dic[id.split(' ')[0]]:
            pass
        else:
            report_dic[id.split(' ')[0]].append(id.split(' ')[1])    
            id_dic[id.split(' ')[1]] += 1
    
    # k 번 이상 신고를 당했으면 out(정지)
    for key, v in id_dic.items():
        if v >= k:
            out_list.append(key)
    
    # 신고한 대상이 정지 되었으면 count
    for id in id_dic.keys():
        count = 0
        for out in out_list:
            if out in report_dic[id]:
                count += 1
        answer.append(count)
            
    return answer

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# Other Solution
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 2023
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    d1 = defaultdict(list)
    d2 = defaultdict(int)
    
    report = list(set(report)) # 중복 제거
    for r in report:
        a, b = r.split(' ')
        d1[a].append(b)
        d2[b] += 1
    
    for idx, id in enumerate(id_list):
        for id_ in d1[id]:
            if d2[id_] >= k:
                answer[idx] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))