def solution(s):
    answer = ''

    m = len(s) // 2

    if len(s) % 2 == 0:
        answer = s[m-1:m+1]
    else:
        answer = s[m]

    return answer

print(solution('abcde'))
print(solution('qwer'))