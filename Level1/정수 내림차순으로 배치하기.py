def solution(n):
    answer = []

    s = str(n)

    for i in s:
        answer.append(i) 
    
    answer = sorted(answer, reverse=True)

    answer = ''.join(answer)

    return int(answer)

print(solution(118372))