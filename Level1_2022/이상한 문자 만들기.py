def solution(s):
    answer = ''

    a = s.split(' ')

    for i in range(len(a)):
        for j in range(len(a[i])):

            if a[i] == '':
                continue
            else:                
                if j % 2 == 0:
                    answer += a[i][j].upper()
                else:
                    answer += a[i][j].lower()
        
        if i < len(a)-1:
            answer += ' '

    
    print(a)
    return answer

print(solution('try hello world'))