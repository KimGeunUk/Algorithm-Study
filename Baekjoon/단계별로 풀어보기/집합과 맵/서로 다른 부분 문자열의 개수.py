word = input().rstrip()

answer = set()
for i in range(1, len(word)+1):
    for j in range(0, len(word)):
        answer.add(word[j:j+i])
print(len(answer))