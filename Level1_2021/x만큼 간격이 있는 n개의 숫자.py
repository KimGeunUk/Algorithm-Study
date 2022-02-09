def solution(x, n):
    answer = []

    sum = 0

    for i in range(n):
        i += 1
        sum += x
        answer.append(sum)

    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))