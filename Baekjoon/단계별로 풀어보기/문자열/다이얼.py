dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'XWYZ']

word = input()
answer = 0
for w in word:
    for idx, d in enumerate(dial, start=3):
        if w in d:
            answer += idx
print(answer)