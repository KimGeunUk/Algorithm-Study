N = int(input())

a, b = 0, 1
s = 1
while True:
    if N > a and N <= b:
        print(s)
        break        
    
    a = b
    b = b + s * 6
    
    s += 1