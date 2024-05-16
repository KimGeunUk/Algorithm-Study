T = int(input())

for t in range(T):
    A, B, C = map(int, input().split())
    
    A, B = min(A, B), max(A, B)
    
    print(f'#{t+1} {(C // A) + ((C % A) // B)}')