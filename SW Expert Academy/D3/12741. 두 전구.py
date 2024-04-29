T = int(input())

answers = []

for t in range(T):
    A, B, C, D = map(int, input().split())
    
    start, end = max(A, C), min(B, D)
    
    if start > end: answers.append(0) # print(f'#{t+1} 0')
    else: answers.append(end - start) # print(f'#{t+1} {end - start}')

for t, answer in enumerate(answers):
    print(f'#{t+1} {answer}')