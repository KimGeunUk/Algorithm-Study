import re

def solution(s):
    answer = []
    
    s_split = list()    
    s_dict = dict()
    
    print(re.split(r'{*}', s))
    

    for i in re.split(r'{*}', s):
        tmp = []     
        if i != '':
            for k in i.split(','):
                if k != '':               
                    tmp.append(re.sub(r"[^0-9]","",k))
        
        if tmp != []:        
            s_split.append(tmp)
            
    # for i in re.split(r'{*}', s):
    #     tmp = ''
    #     if i == '':
    #         continue
    #     else:
    #         for j in i:
    #             if j.isdigit():
    #                 tmp += j
    #     s_split.append(tmp)
    
    # print(s_split)
    
    for i in s_split:
        for j in i:
            if j in s_dict:
                s_dict[j] += 1
            else:
                s_dict[j] = 1
    
    sorted_dict = sorted(s_dict.items(), key = lambda x: x[1], reverse=True)
    
    answer = [int(i[0]) for i in sorted_dict]  
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
