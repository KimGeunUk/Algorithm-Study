""" 
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5

와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항 : 
    n은 2 이상 100,000 이하인 자연수입니다.
"""
import time

def fib(n):
    start = time.time() 
    
    n_0, n_1 = 0, 1
    for _ in range(n):
        n_0, n_1 = n_1, n_0 + n_1    
        
    return round(time.time() - start, 4)

def fib1(n):
    start = time.time() 
    d = [0]*50000
    
    if n==1 or n==2:
        return 1
    if d[n] != 0:
        return d[n]
    
    d[n] = fib1(n-1) + fib(n-2)
    return round(time.time() - start, 4)

print(fib1(49999))
