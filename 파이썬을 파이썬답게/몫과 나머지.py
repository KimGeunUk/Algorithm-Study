# 다른 언어
def solution(str1):
    a, b = map(int, str1.strip().split(' '))
    return int(a//b), a%b

# divmod - 큰 수를 다룰때 유용
def solution(str1):
    a, b = map(int, str1.strip().split(' '))
    return (divmod(a, b))
    

print(solution('5 3'))