def fib1(N):
    global count1
    
    if N == 1 or N == 2:
        count1 += 1
        return 1
    else:
        return (fib1(N-1) + fib1(N-2))

def fib2(N):
    global count2
    
    a, b = 0, 1
    for _ in range(N):
        count2 += 1
        a, b = b, a + b
    return a

N = int(input())

count1 = 0
count2 = 0

fib1(N)
fib2(N)

print(count1, count2-2)