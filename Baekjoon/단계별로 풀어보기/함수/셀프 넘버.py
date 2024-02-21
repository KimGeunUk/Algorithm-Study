all_ = [i for i in range(1, 10001)]
for i in range(1, 10001):    
    for j in str(i):
        i += int(j)
    
    if i in all_:
        all_.remove(i)

for i in all_:
    print(i)