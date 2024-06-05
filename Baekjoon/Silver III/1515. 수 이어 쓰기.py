string = input().strip()

def func():    
    i = 0
    now = 0
    
    while True:
        now += 1        
        for n in str(now):
            if string[i] == n:
                i += 1
                if i >= len(string):
                    return now

print(func())