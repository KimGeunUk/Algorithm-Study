n, m = map(int, input().split())
j = int(input())

count = 0

start = 1
end = m

for _ in range(j):
    k = int(input())
    
    while True:
        if k in range(start, end+1):
            break
        
        count += 1
        
        if k > end:            
            start += 1
            end += 1
        elif k < start:
            start -= 1
            end -= 1
    
print(count)