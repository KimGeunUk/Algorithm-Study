def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))

    for idx, row in enumerate(data[row_begin-1:row_end]):
        row_sum = 0
        for r in row:         
            row_sum += r % (idx+row_begin)
        answer = answer ^ row_sum

    return answer


print(solution([[2,2,6],
                [1,5,10],
                [4,2,9],
                [3,8,3]], 2, 2, 3)) # 4