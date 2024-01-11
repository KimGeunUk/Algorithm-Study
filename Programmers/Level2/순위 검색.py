from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    DB = {}
    
    for i in info:
        info_ = i.split()
        score = int(info_[-1])
        conditions = info_[:-1]
        
        for n in range(5):
            c = list(combinations(range(4), n))
            for c_ in c:
                conditions_ = conditions.copy()
                for v in c_:
                    conditions_[v] = '-'
                conditions_ = ''.join(conditions_)
                if conditions_ in DB:
                    DB[conditions_].append(score)
                else:
                    DB[conditions_] = [score]
                    
    for v in DB.values():
        v.sort()

    for q in query:
        q = q.replace("and ", "").split()
        DB_key = ''.join(q[:-1])
        DB_score = int(q[-1])

        if DB_key in DB:
            data = DB[DB_key]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= DB_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)
        
    return answer

# bisect 함수 사용
def solution(info, query):
    answer = [0 for _ in range(len(query))]
    info_list = list()
    query_list = list()
        
    for idx, (i, q) in enumerate(zip(info, query)):
        info_list.append(i.split())
        query_list.append(q.replace('and', '').split())

    for idx, query in enumerate(query_list):
        for info in info_list:
            if int(query[4]) <= int(info[4]):
                for i in range(4):
                    if query[i] == "-":
                        continue
                    elif query[i] != info[i]:
                        break
                else:
                    answer[idx] += 1
    return answer

print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"])) # [1,1,1,1,2,4]