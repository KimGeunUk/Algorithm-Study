T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    
    print(f'#{t+1} {(A + B) % 24}')