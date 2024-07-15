import sys
input = sys.stdin.readline

H, W = map(int, input().split())
infos = [list(input().strip()) for _ in range(H)]

answers = []
for info in infos:
    temp = -1
    answer = []    
    for idx, i in enumerate(info):
        if i == 'c':
            temp = 0
        else:
            if temp != -1:
                temp += 1
        answer.append(temp)    
    answers.append(answer)
    
for answer in answers:
    print(*answer)