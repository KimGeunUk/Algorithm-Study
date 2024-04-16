from collections import Counter

T = int(input())

for _ in range(T):
    i = int(input())
    numbers = map(int, input().split())
    
    c = Counter(numbers)
    
    print(f'#{i} {sorted(c.items(), key=lambda x: (x[1], x[0]))[-1][0]}')