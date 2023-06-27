def solution(N, stages):
    answer = []

    success = [0]*(N+1)
    successful = []

    count = len(stages)

    for i in stages:
        success[i-1] += 1

    for i in range(len(success)-1):

        if success[i] == 0:
            successful.append((i+1,0))
        else:
            successful.append((i+1,success[i]/count))
        count -= success[i]
   
    #successful 의 두 번째 인자를 내림차순으로
    successful = sorted(successful, key = lambda x: x[1], reverse=True)
    
    answer = [x[0] for x in successful]
    
    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))
print(solution(4,[4,4,4,4,4]))

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
# list = sorted(e, key = lambda x : (x[0], -x[1]))