T = int(input())

for i in range(1, T + 1):
    sentence = input().strip()
    
    word = ''
    
    for idx, alpha in enumerate(sentence):
        word += alpha

        if word == sentence[idx+1:idx+1+len(word)]:
            print(f'#{i} {idx+1}')
            break
        