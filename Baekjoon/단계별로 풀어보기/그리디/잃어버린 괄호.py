s = input().split('-')

count = 0
for i in s[0].split('+'):
    count += int(i)
    
for i in s[1:]:
    for j in i.split('+'):
        count -= int(j)

print(count)