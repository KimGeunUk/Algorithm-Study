# 자카드 유사도 : 집합 간의 유사도 검사
# - 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# - 두 집합 모두 공집합일 경우 J(A, B) = 1
# - 중복이 있을 때 교집합의 경우 min(중복 A의 개수, 중복 B의 개수) 합집합의 경우 max(중복 A의 개수, 중복 B의 개수)
# - 문장의 경우 두글자씩 끊어서 유사도 측정 / 기타 공백이나 숫자, 특수 문자가 포함되어 있을 경우 쌍을 버린다.
def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower() 
    
    str1_list = []
    str2_list = []
    
    for idx, s1 in enumerate(str1):        
        if idx < len(str1)-1:
            if str1[idx].isalpha()==False or str1[idx+1].isalpha()==False:
                pass
            else:
                str1_list.append(str1[idx])
                str1_list[-1] += str1[idx+1]
            
    for idx, s2 in enumerate(str2):        
        if idx < len(str2)-1:
            if str2[idx].isalpha()==False or str2[idx+1].isalpha()==False:
                pass
            else:
                str2_list.append(str2[idx])
                str2_list[-1] += str2[idx+1]
                
    if str1_list == [] and str2_list == []:
            return 65536
                
    union_list = []
    inter_list = []
    
    for i in str1_list:
        if i in str2_list:
            if i in inter_list:
                pass
            else:
                count1 = str1_list.count(i)
                count2 = str2_list.count(i)
                
                for j in range(min(count1, count2)):                 
                    inter_list.append(i)
                for j in range(max(count1, count2)):              
                    union_list.append(i)
        else:
            union_list.append(i)
            
    for i in str2_list:
        if i not in union_list:
            count = str2_list.count(i)
            for j in range(count):
                union_list.append(i)
                        
    answer = int((len(inter_list) / len(union_list))*65536)
    
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution(' abc', 'abbb'))

# 다른 사람 풀이 - 정말 깔끔하다..
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)