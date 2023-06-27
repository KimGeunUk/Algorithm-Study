def solution(phone_number):
    answer = ''

    for i in phone_number[:-4]:
        answer += '*'
    
    for i in phone_number[-4:]:
        answer += i

    return answer

print(solution('01033334444'))
print(solution('027778888'))