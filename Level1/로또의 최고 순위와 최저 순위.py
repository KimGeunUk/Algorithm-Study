def solution(lottos, wins):
    answer = []
    sorted_lottos = sorted(lottos)
    win = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    zero_count = lottos.count(0)
    win_count = 0
    
    if zero_count >= 1:
        for i in range(zero_count):
            sorted_lottos.remove(0)
    
    for i in sorted_lottos:
        if i in wins:
            win_count += 1
    
    answer.append(win[win_count+zero_count])
    answer.append(win[win_count])
    
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))