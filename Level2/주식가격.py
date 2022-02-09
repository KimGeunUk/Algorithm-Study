def solution(prices):
    answer = [0] * len(prices)

    count = 0

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                if i != len(prices)-1:
                    count += 1
                break
            else:
                count += 1

        answer[i] = count
        count = 0

    return answer

print(solution([1, 2, 3, 2, 3, 1]))
#[5, 4, 1, 2, 1, 0]