import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return -1
    elif n == 2:
        return 1
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return -1
    else:
        return 1

A = int(input())
B = int(input())
    
s = []
for n in range(A, B+1):
    if isPrime(n) == 1:
        s.append(n)

if len(s) == 0: print(-1)
else:
    print(sum(s))
    print(min(s))