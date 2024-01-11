def solution(answers):

    answer = []

    a = [1,2,3,4,5]
    counta=0
    b = [2,1,2,3,2,4,2,5]
    countb=0
    c = [3,3,1,1,2,2,4,4,5,5]
    countc=0

    for i in range(len(answers)):
        
        a1 = i%5
        b1 = i%8
        c1 = i%10

        if answers[a1] == a[i]:
            counta += 1

        if answers[b1] == b[i]:
            countb += 1

        if answers[c1] == c[i]:
            countc += 1

    m = max(counta,countb,countc)

    if m == counta:
        answer.append(1)
    
    if m == countb:
        answer.append(2)
    
    if m ==countc:
        answer.append(3)
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

#런타임 에러...