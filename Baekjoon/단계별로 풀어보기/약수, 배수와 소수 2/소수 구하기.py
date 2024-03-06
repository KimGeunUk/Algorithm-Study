import sys
input = sys.stdin.readline

import math
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True
    
M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)