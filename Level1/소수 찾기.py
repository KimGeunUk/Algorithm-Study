def solution(n):
    answer = 0
    
    count = 0
    
    for i in range(2, n+1):
        for j in range(2, i+1):
            if i%j == 0:                
                count += 1 
                
        if count == 1:
            answer +=1
            
        count = 0
    
    return answer

    #시간 초과 실패

def solution2(n):  

    count = 0
    
    for n in range(2, n+1):
        for j in range(2, n):
            if n%j == 0:                
                break                
        else:
            count += 1
            
    return count

    #이것도 시간 초과 실패

def solution3(n):
    num = set(range(2,n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    
    return (num)
    
    # 앞에서 부터 그 수의 배수 제거
    

print(solution3(10))
print(solution3(5))