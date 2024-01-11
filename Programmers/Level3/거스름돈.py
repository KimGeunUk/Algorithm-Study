def solution(n, money):
    answer = 0
    
    DP = [1] + [0] * (n)
    
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                DP[i] += DP[i - m]
    
    return answer

print(solution(5, [1, 2, 5])) # 4