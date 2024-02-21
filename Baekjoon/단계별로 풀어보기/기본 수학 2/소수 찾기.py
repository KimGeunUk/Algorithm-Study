import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return -1
    elif n == 2:
        return 1
    
    for i in range(2, n // 2 + 1):
        print(i)
        if n % i == 0:
            return -1
    else:
        return 1

N = int(input())
nums = list(map(int, input().split()))
    
s = 0
for n in nums:
    if isPrime(n) == 1:
        s += 1
        
print(s)