def fac(n):
    answer = 1
    
    if n > 0:
        answer = n * fac(n-1)
    
    return answer

N = int(input())

print(fac(N))
