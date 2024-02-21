import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    l = input()
    answer = 0
    count = 0
    
    for l_ in l:
        if l_ == 'O':
            count += 1
            answer += count
        elif l_ == 'X':
            count = 0
                        
    print(answer)