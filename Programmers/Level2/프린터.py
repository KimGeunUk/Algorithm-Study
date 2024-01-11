def solution(priorities, location):
    answer = 0
    a = []

    for i, j in zip(range(len(priorities)), priorities):
        a.append([i, j])

    b = sorted(priorities, reverse=True)

    i = 0
    while i != len(priorities):
        if a[i][1] != b[i]:
            c = a.pop(i)
            a.append(c)
        else:
            i += 1

    a.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(a)):
        if location == a[i][0]:
            answer = i + 1

    return answer

print(solution([1, 2, 3, 2], 2))            # 1
print(solution([1, 1, 9, 2, 1, 1], 0))      # 5