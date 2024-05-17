T = int(input())

for t in range(T):
    s = list(map(int, list(input().strip())))
    
    sum_ = 0
    answer = 0
    
    for idx, n in enumerate(s, start=1):
        if n == 0: continue

        if sum_ < (idx - 1):
            answer += (idx - 1) - sum_
            sum_ += (idx - 1) - sum_    
            
        sum_ += n    

    print(f'#{t+1} {answer}')