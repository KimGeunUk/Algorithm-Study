import sys
input = sys.stdin.readline

T = int(input())

numbers = [int(input()) for _ in range(T)]

n = max(numbers)

primes = [True] * (n + 1)

for i in range(2, int(n**0.5)+1):
    if primes[i]:
        for j in range(i*2, n+1, i):
            primes[j] = False

for number in numbers:    
    count = 0
    for i in range(2, int(number//2)+1):
        if primes[i] and primes[number-i]:
            count += 1   
                
    print(count)