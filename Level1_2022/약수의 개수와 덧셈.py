def common_division(num):
    cd_list = []

    for i in range(1, num//2 + 1):
        if num % i == 0:
            cd_list.append(i)
            cd_list.append(int(num/i))
            
    return len(sorted(set(cd_list)))

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if i == 1:
            answer -= 1
        elif common_division(i) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

print(solution(13, 17))
print(solution(24, 27))
print(solution(1, 2))

# 제곱한 수의 약수는 홀수개로 고정.. 맞네 ? 나는 바보임에 틀림없다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer