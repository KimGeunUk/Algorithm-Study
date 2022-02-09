def solution(d, budget):
    answer = 0
    sum = 0

    d.sort()

    for i in range(len(d)):        
        while True: 
            sum += d[i]
            answer += 1
            
            i += 1

            if i >= len(d):
                i = 0

            if sum == budget:
                break
            elif sum >= budget:                
                answer -= 1
                break

    print(d)

    return answer
    # 4개 오류가 난다 ;


def solution2(d, budget):
    answer = 0

    sum = 0

    d.sort()

    for i in range(len(d)):
        sum += d[i]

        if sum <= budget:
            if sum == budget:
                answer += 1
                break
            else:
                answer += 1        
            
    return answer

    #성공

print(solution2([1,3,2,5,4], 9))
print(solution2([2,2,3,3], 10))