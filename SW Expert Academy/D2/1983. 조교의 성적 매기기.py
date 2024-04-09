import math

T = int(input())

grade = {1: 'A+', 2: 'A0', 3: 'A-', 4: 'B+', 5: 'B0', 6: 'B-', 7: 'C+', 8: 'C0', 9: 'C-', 10: 'D0'}

for i in range(1, T + 1):
    
    N, K = map(int, input().split())
    
    scores = []
    
    for j in range(1, N + 1):
        A, B, C = map(int, input().split())
        
        scores.append([j, A * 0.35 + B * 0.45 + C * 0.2])
    
    scores = sorted(scores, key=lambda x: -x[1])
    
    for idx, score in enumerate(scores, start=1):
        if score[0] == K:
            print(f'#{i} {grade[math.ceil(idx / (N // 10))]}')
            break