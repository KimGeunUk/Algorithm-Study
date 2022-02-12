import math
def solution(answers):
    answer = []
    
    a = [1,2,3,4,5]
    acount=0
    b = [2,1,2,3,2,4,2,5]
    bcount=0
    c = [3,3,1,1,2,2,4,4,5,5]
    ccount=0
    
    len_answers = len(answers)
    
    if len(a) < len_answers:
        a = a*math.ceil(len_answers/len(a))
    if len(b) < len_answers:
        b = b*math.ceil(len_answers/len(b))       
    if len(c) < len_answers:
        c = c*math.ceil(len_answers/len(c))
    
    for answer_i, a_i, b_i, c_i in zip(answers, a, b, c):
        if answer_i == a_i:
            acount +=1
        if answer_i == b_i:
            bcount +=1
        if answer_i == c_i:
            ccount +=1
            
    max_count = max(acount, bcount, ccount)
    
    if max_count == acount:
        answer.append(1)
    if max_count == bcount:
        answer.append(2)
    if max_count == ccount:
        answer.append(3)
    
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5,1,2]))

# 뭔가 좀 난잡한 코드다..
# 아래 코드 방식은 처음에 생각했던 방식인데 왜 까먹었찌

# Other Solution

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result