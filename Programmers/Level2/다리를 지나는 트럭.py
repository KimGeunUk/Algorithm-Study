def solution(bridge_length, weight, truck_weights):
    answer = 0
    length = [0] * bridge_length            # 핵심 지나가는 트럭의 리스트를 확인할 수 있도록

    while True:
        answer += 1

        length.pop(0)

        if len(truck_weights) != 0:
            if sum(length) + truck_weights[0] <= weight:
                length.append(truck_weights.pop(0))
            else:
                length.append(0)
        elif len(truck_weights) == 0 and sum(length) == 0:
            break

    return answer

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))