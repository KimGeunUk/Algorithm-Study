"""
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
스파이는 하루에 최소 한 개의 의상은 입습니다.
"""

import itertools
def solution(clothes):
    answer = 0
    
    cloth_dic = dict()
    
    for cloth in clothes:
        if cloth[1] in cloth_dic:
            cloth_dic[cloth[1]].append(cloth[0])
        else:
            cloth_dic[cloth[1]] = [cloth[0]]

    v_list = list()
    v_len = list()
    
    for v in cloth_dic.values():
        answer += len(v)
        v_list.append(v)
        v_len.append(len(v))

    if len(cloth_dic.keys()) == 1:
        return answer
    if max(v_len) == 1:
        answer = 0
        for i in range(len(v_len)):
            answer += pow(2,i)
        return answer
    
    for i in range(2, len(v_list)+1):
        v_list_ = list(itertools.combinations(v_list, i))
        for j in v_list_:
            answer += len(list(itertools.product(*j)))

    return answer

def solution1(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

def solution2(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

# 다음 원리를 사용하면 쉽게 풀 수 있다.
# (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc 

print(solution1([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["aa", "bb"]])) # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3
print(solution1([[1, 'a'], [2, 'b']]))
print(solution([[1, 'a'], [2, 'b'], [3, 'c']]))
#print(solution([[1, 'a'], [4, 'a'], [2, 'b'], [5, 'b'], [3, 'c'], [6, 'c']])) # 4 + 7