a = input()
origin = a
c = 0
while True:
    if int(a) >= 10:
        a = a[1] + str(int(a[0]) + int(a[1]))[-1]
    else:
        a = a[-1] + a[-1]
    c += 1
    
    if int(a) == int(origin):
        break
        
print(c)
    