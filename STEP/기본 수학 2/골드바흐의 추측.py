from math import sqrt

Limit = 10000
PrimeList = [True] * (Limit + 1)
PrimeList[0], PrimeList[1] = False, False

for i in range(2, int(sqrt(Limit) + 1)):
    if PrimeList[i]:
        j = 2
        while (i * j) < Limit + 1:
            PrimeList[i * j] = False
            j += 1

T = int(input())
for _ in range(T):    
    N = int(input())
        
    answer = ''
    diff = float('inf')
    for i in range(2, N):
        if PrimeList[i] and PrimeList[N-i]:
            if diff > abs(N-i-i):
                answer = str(i) + ' ' + str(N-i)
                diff = abs(N-i-i)
    print(answer)
                
    