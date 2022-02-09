def solution(n):
    answer = []

    s = str(n)

    for i in range(1,len(s)+1):
        answer.append(int(s[-i]))    

    return answer

print(solution(12345))