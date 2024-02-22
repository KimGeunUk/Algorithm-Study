N = int(input())

answer = 0
for _ in range(N):
    word = input()
    
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            i += 1
        else:
            if word[i-1] in word[i:]:
                break
    else:
        answer += 1
        
print(answer)