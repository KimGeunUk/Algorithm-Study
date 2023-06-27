def solution(s, n):
    answer = ''

    a = 0

    for i in s:

        if i == ' ':
            answer += ' '

        elif ord(i) >= 97 and ord(i) < 123:

            a = ord(i) + n

            if a > 122:
                a = a - 26
            
            answer += chr(a)

        elif ord(i) >= 65 and ord(i) <= 90 :

            a = ord(i) + n

            if a > 90:
                a = a - 26

            answer += chr(a)

    print(ord('['))

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))