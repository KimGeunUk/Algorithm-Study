N = int(input())

c = 1
s = 0

while True: 
    s += c    
    if N > s-c and N <= s:
        if c % 2 == 0:
            a, b = 1, c
            for i in range(c - (s - N) -1):
                a, b = a + 1, b - 1
        else:
            a, b = c, 1
            for i in range(c - (s - N) -1):
                a, b = a - 1, b + 1
        break    
    c += 1
    
print(str(a)+'/'+str(b))