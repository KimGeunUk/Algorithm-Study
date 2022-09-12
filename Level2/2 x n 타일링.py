import math
def solution(n):
    answer = 1
    
    if n == 1:
        return 1
    
    answer += n - 1
    
    count = 2
    
    while True:
        m = n - (2*count)
        
        if m == 0:            
            answer += 1
            break
        elif m < 0:
            break
        else:
            answer += math.factorial(n-count) / (math.factorial(m) * math.factorial(count))
            
        count += 1
        
    return int(answer) % 1000000007

# 피보나치 수열!
def fib(n):    
    _curr, _next = 0, 1
    for _ in range(n+1):
        _curr, _next = _next, _curr + _next
    return _curr % 1000000007

print(fib(3))

print(solution(3)) # 3
print(solution(4)) # 5
print(solution(5)) # 8
print(solution(6)) # 13
print(solution(7)) # 21
print(solution(8)) # 34
print(solution(9)) # 55
