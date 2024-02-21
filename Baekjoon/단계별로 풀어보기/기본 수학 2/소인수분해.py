import math

N = int(input())

while True:    
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            print(i)
            N = N // i
            break
    else:
        if N != 1:
            print(N)
        break
