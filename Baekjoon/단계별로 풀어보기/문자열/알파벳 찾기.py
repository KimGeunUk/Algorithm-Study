word = input()

answer = [-1 for _ in range(26)]
for idx, w in enumerate(word):
    if answer[ord(w)-97] == -1:
        answer[ord(w)-97] = idx
print(' '.join(map(str, answer)))