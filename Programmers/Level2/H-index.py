""" 
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항 : 
    과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
    논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
"""

def solution(citations):
    answer = []

    b_l = []
    for i in range(max(citations)):
        u = 0
        d = 0
        
        for j in citations:
            if i <= j:
                u += 1
            else:
                if i >= j:
                    d += 1
                    
        if u >= i and d <= i:
            b_l.append(i)
            if u == i:
                answer.append(u)

    if answer == []:
        if len(b_l) == 0:
            return 0
        return min(b_l)
    
    return max(answer)

# 다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

#print(solution([3, 0, 6, 1, 5])) # 3
print(solution([6, 5, 5, 5, 3, 2, 1, 0])) # 4
print(solution([1,4])) # 1
print(solution([0,1,2])) # 1