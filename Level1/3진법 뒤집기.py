def solution(n):
    answer=0

    s=[]

    while n != 0:
        s.append(n % 3)
        n //= 3

    for i in range(1,len(s)+1):
        answer += s[-i] * 3 ** (i-1)

    return answer

print(solution(45))
print(solution(125))