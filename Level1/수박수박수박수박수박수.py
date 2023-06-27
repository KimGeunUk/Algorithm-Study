def solution(n):
    answer = ''

    for i in range(n):
        i += 1
        answer += "수박"
    return answer[:n]

print(solution(3))
print(solution(4))