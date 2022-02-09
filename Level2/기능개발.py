def solution(progresses, speeds):
    answer = []
    end = []

    for i, j in zip(progresses, speeds):
        count = 0
        while i < 100:
            count += 1
            i += j
        end.append(count)
    print(end)

    i = 0
    m = 0

    while True:
        count = 0
        for j in range(i, len(end)):
            if end[i] >= end[j]:
                count += 1
                if j == len(end) - 1:
                    answer.append(count)
                    m = i
            else:
                i = j
                break

        if m == i:
            break
        else:
            m += 1
            answer.append(count)

        # 더 쉬운 방법이 있는데..

    return answer

print(solution([93, 30, 55], [1, 30, 5]))                           #[2, 1]
print(solution([95, 90, 99, 99, 80, 90], [1, 1, 1, 1, 1, 1]))       #[1, 3, 2]