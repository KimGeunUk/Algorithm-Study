T = int(input())

for t in range(T):
    N = int(input())
    answer = -1
    
    for i in range(1, N+1):
        if i ** 3 > N:
            break
        
        if i ** 3 == N:
            answer = i
            break
        
    print(f'#{t+1} {answer}')