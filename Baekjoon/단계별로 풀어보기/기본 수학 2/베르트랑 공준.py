# import math
# def isPrime(n):
#     if n == 1:
#         return False
    
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     else:
#         return True

# while True:
#     N = int(input())
#     if N == 0:
#         break
    
#     c = 0
#     for i in range(N+1, 2*N+1):        
#         if isPrime(i):
#             c += 1
#     print(c)
import math

Limit = 123456
PrimeList = [True] * ((Limit*2) + 1)
PrimeList[0], PrimeList[1] = False, False

for i in range(2, int(math.sqrt(2*Limit) + 1)):
    if PrimeList[i]:
        j = 2
        while (i * j) <= (2 * Limit) + 1:
            PrimeList[i * j] = False
            j += 1
            
while True:
    N = int(input())
    if N == 0:
        break
    
    c = 0
    for i in range(N+1, 2*N+1):        
        if PrimeList[i]:
            c += 1
    print(c)