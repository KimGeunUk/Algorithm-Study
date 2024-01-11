def solution(n, lost, reserve):
    answer=0
    count=0
    student = []

    for i in range(n):
        student.append(1)
    
    for i in range(len(lost)):
        student[lost[i]-1] -= 1
    
    for i in range(len(reserve)):
        student[reserve[i]-1] += 1
    
    for i in range(len(student)):
        if i > 0 and i < len(student)-1:
            if student[i] == 0:
                if student[i-1] > 1:
                    student[i-1] -= 1
                    student[i] += 1
                elif student[i+1] > 1:
                    student[i+1] -= 1
                    student[i] += 1
        elif i == 0:
            if student[i] == 0:
                if student[i+1] > 1:
                    student[i+1] -= 1
                    student[i] += 1
        elif i == len(student)-1:
            if student[i] == 0:
                if student[i-1] > 1:
                    student[i-1] -= 1
                    student[i] += 1
    
    for i in student:
        if i >= 1:
            count += 1
    
    answer = count
        
    return answer

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))