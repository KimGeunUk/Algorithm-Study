def solution(n, arr1, arr2):
    answer = []

    a1 = [0]*n
    a2 = [0]*n

    map1 = [[0]*n for _ in range(n)]


    for i in range(n):
        if len(format(arr1[i],'b')) != n:            
            a1[i] = '0'*(n-len(format(arr1[i],'b'))) + format(arr1[i],'b')
        else:
            a1[i] = format(arr1[i],'b')

        if len(format(arr2[i],'b')) != n:            
            a2[i] = '0'*(n-len(format(arr2[i],'b'))) + format(arr2[i],'b')
        else:
            a2[i] = format(arr2[i],'b')

    for i in range(n):
        for j in range(n):
            if a1[i][j] != str(1) and a2[i][j] != str(1):
                map1[i][j] = ' '
            else:
                map1[i][j] = '#'
    
    for i in range(n):        
       answer.append(''.join(map1[i]))            
    
    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]))