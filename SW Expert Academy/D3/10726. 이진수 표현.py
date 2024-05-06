T = int(input())

answers = []
for t in range(T):
    N, M = map(int, input().split())
    
    if sum(map(int, list(f'{M:030b}'[-N:]))) == N:
        answers.append(f'#{t+1} ON')
    else:
        answers.append(f'#{t+1} OFF')

for answer in answers:
    print(answer)