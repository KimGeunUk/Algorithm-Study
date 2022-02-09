# 내적 : 두 벡터를 표준기저벡터로 나타내었을 때 각 성분끼리의 곱의 합

def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))