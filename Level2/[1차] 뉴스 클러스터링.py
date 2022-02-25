# 자카드 유사도 : 집합 간의 유사도 검사
# - 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# - 두 집합 모두 공집합일 경우 J(A, B) = 1
# - 중복이 있을 때 교집합의 경우 min(중복 A의 개수, 중복 B의 개수) 합집합의 경우 max(중복 A의 개수, 중복 B의 개수)
# - 문장의 경우 두글자씩 끊어서 유사도 측정 / 기타 공백이나 숫자, 특수 문자가 포함되어 있을 경우 쌍을 버린다.
def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = [i for i in str1 if i.isalpha()==True]
    str2 = [i for i in str2 if i.isalpha()==True]   
    
    str1_list = []
    str2_list = []
    str1_dic = {}
    str2_dic = {}
    
    for idx, s1 in enumerate(str1):        
        if s1.isalpha() == True and idx < len(str1)-1:
            str1_list.append(str1[idx])
            str1_list[idx] += str1[idx+1]
            
    for idx, s2 in enumerate(str2):        
        if s2.isalpha() == True and idx < len(str2)-1:    
            str2_list.append(str2[idx])
            str2_list[idx] += str2[idx+1]
    
    print(str1_list)
    print(str2_list)
    
    union_list = []
    inter_list = []
    
    if len(str1_list) > len(str2_list):
        for i in str2_list:
            if i in str1_list:
                inter_list.append(i)
            else:
                union_list.append(i)
        union_list += str1_list        
    else:
        for i in str1_list:
            if i in str2_list:
                count1 = str1_list.count(i)
                count2 = str2_list.count(i)
                print(count1, count2)
                inter_list.append(i)
            else:
                union_list.append(i)
        union_list += str2_list
    
    print(inter_list)
    print(union_list)
    
    return answer

#print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
#print(solution('aa1+aa2', 'AAAA12'))
#print(solution('E=M*C^2', 'e=m*c^2'))