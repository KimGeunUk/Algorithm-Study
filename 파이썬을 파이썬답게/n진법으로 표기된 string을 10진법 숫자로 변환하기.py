# 다른 언어
def solution(str1):
    answer = 0
    a, b = map(int, str1.strip().split(' '))
    for i in range(len(str(a))):
        if i == len(str(a))-1:
            answer += int(str(a)[i])*pow(b, 0)
        else:
            answer += int(str(a)[i])*pow(b, len(str(a))-(i+1))
   
    return answer

# int(x, base=10)

def solution(str1):
    a, b = map(int, str1.strip().split(' '))
    return int(str(a), base=10)

print(solution('121 2'))
#print(solution('12 2'))
#print(solution('444 10'))