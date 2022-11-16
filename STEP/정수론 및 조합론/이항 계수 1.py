# def fac(n):
#     answer = 1    
#     if n > 0:
#         answer = n * fac(n-1)    
#     return answer
import math

def fac(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer 

N, K = map(int, input().split())

print( int((math.factorial(N) // (math.factorial(K) * math.factorial(N-K)))) % 10007)