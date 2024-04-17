T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    answer = 0
    
    words = [input().strip() for _ in range(N)]
    
    trigger = False
    
    while words:
        word = words.pop()
        
        if word[::-1] in words:
            words.remove(word[::-1])
            answer += M * 2
        elif trigger == False:
            len_word = len(word)
            
            if len_word % 2 != 0:
                A = word[:(len_word-1)//2]
                B = word[(len_word-1)//2 + 1:]
            else:
                A = word[:(len_word-1)//2 + 1]
                B = word[(len_word-1)//2 + 1:]

            if A == B[::-1]:
                answer += M
                trigger = True
    
    print(f'#{i+1} {answer}')