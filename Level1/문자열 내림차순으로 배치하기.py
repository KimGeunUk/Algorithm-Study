def solution(s):
    
    #대문자는 소문자보다 작은 것으로 간주

    answer = ''

    s = sorted(s, reverse=True)

    answer = ''.join(s)

    return answer

print(solution('Zbcdefg'))