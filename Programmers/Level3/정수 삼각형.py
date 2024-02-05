def solution(triangle):
    for i, tri in enumerate(triangle[1:]):
        for j, t in enumerate(tri):
            a, b = j - 1, j # 한 칸 위의 왼쪽 오른쪽
            
            if j == 0:
                max_ = triangle[i][b]
            elif j == i+1:
                max_ = triangle[i][a]
            else:
                max_ = max(triangle[i][a], triangle[i][b])
            
            triangle[i+1][j] = t + max_

    return max(triangle[-1])

print(solution([[7], 
                [3, 8], 
                [8, 1, 0], 
                [2, 7, 4, 4], 
                [4, 5, 2, 6, 5]])) # 30