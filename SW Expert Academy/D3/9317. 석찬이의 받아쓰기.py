T = int(input())

for t in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    count = 0
    
    for a, b in zip(A, B):
        if a == b:
            count += 1
    
    print(f'#{t+1} {count}')