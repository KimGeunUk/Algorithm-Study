def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]

    sum = 0
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            sum = arr1[i][j] + arr2[i][j]
            
            answer[i][j] = sum

    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))