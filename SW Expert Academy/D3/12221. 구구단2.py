T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    
    if 1 <= A <= 9 and 1 <= B <= 9:
        print(f'#{t+1} {A * B}')
    else:
        print(f'#{t+1} -1')