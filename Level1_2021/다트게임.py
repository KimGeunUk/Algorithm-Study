def solution(dartResult):
    answer = 0
    count = 0
    num = 0
    sum = []

    for i in range(len(dartResult)):
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if dartResult[i] == 'S':
                sum.append(num**1)
                num = 0
            elif dartResult[i] == 'D':
                sum.append(num**2)
                num = 0
            elif dartResult[i] == 'T':
                sum.append(num**3)
                num = 0
                
            count += 1

        elif dartResult[i] == '*' or dartResult[i] == '#':
            if dartResult[i] == '*':
                if count <= 1:
                    sum[count-1] = sum[count-1]*2
                else:
                    sum[count-2] = sum[count-2]*2
                    sum[count-1] = sum[count-1]*2
            else:
                sum[count-1] = -sum[count-1]

        elif dartResult[i] == '0':
            continue

        else:
            if i < len(dartResult)-2:
                if dartResult[i]+dartResult[i+1] == '10':
                    num = int(10)                               
                else:
                    num = int(dartResult[i])
            else:
                num = int(dartResult[i])

        # 10 을 처음부터 문자열을 읽어 새로 문자열을 만들면 더 편할듯
 
    for i in sum:
        answer += i

    return answer

print(solution('10S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
