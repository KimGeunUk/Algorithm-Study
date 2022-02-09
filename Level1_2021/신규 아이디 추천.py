new_id = input()

answer = []

new_id = new_id.lower()

count = 0

for i in new_id:
    if i.isalnum() or i == '-' or i == '_' or i == '.':
        answer.append(i)

while True:
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            answer = answer[:i] + answer[i+1:]
            break    
    count += 1    
    if count == len(answer):
        break

if answer[0] == '.':    
    answer = answer[1:]    

if len(answer) == 0:
    answer ='a'

if answer[-1] == '.':
    answer = answer[:-1]

if len(answer) == 0:
    answer ='a'

if len(answer) >= 16:
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

if len(answer) < 3:
    answer += answer[-1] * (3 - len(answer))

#answer = new_id

print(''.join(answer))

#미완성
