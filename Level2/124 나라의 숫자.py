def solution(n):
    answer = ''

    # 1번 방법
    # while n > 0:
    #     n -= 1
    #     answer = '124'[n%3] + answer
    #     n //= 3

    # 2번 방법
    while n > 0:
        if n % 3 == 0:
            answer = '4' + answer
            n = int(n / 3) - 1
        else:
            answer = str(n % 3) + answer
            n = int(n / 3)

    return answer

print(solution(1))
print(solution(2))
print(solution(13))
print(solution(15))
print(solution(22))
