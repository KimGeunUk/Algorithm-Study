def divisor(num):
    s = set()
    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            s.add(num//i)
            s.add(i)
    return len(s)
        

def solution(number, limit, power):
    answer = 0

    for n in range(1, number+1):        
        if divisor(n) > limit:
            answer += power
        else:
            answer += divisor(n)

    return answer

print(solution(5, 3, 2))
print(solution(10, 3, 2))
