import sys
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == -1: break
    
    _sum = [1]
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:            
            _sum.extend([i, int(n//i)])
    
    if sum(_sum) == n:
        _sum = sorted(_sum)
        print(f"{n} = ", end='')
        print(" + ".join(map(str, _sum)))
    else:
        print(f"{n} is NOT perfect.")
        
        
    