def fac(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer 

N = int(input())

sN = str(fac(N))

answer = 0
for n in sN[::-1]:
    if n != '0':
        break    
    answer += 1
    
print(answer)