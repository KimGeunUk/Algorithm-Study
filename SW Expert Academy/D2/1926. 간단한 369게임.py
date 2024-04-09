from collections import Counter

N = int(input())

for i in range(1, N + 1):
    c = Counter(str(i))
    
    count = c['3'] + c['6'] + c['9']
    
    if count > 0:
        print('-' * count, end=' ')
    else: print(i, end=' ')