T = int(input())

for t in range(T):
    N = int(input())
    S = ''
    while True:
        S += input()
        count = S.count('.') + S.count('?') + S.count('!') 
        if count == N: break

    S = S.split()
    answer = []
    count = 0
    
    for i in range(len(S)):
        w = S[i].rstrip(".!?")        
        if w.isalpha():
            if w[0].isupper() and w[1:].islower(): count += 1
            if len(w) == 1 and w[0].isupper(): count += 1
        
        if S[i][-1] in [".", "!", "?"]:
            answer.append(count)
            count = 0
    
    print(f'#{t+1} ', end='')
    print(' '.join(map(str, answer)))