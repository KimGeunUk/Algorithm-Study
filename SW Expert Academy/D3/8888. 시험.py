TC = int(input())

for t in range(TC):
    N, T, P = map(int, input().split())
    
    solved = [list(map(int, input().split())) for _ in range(N)]
    
    solves = [0 for _ in range(N)]
    scores = [0 for _ in range(N)]
    grades = [1 for _ in range(N)]    
    
    for i, solve in enumerate(solved):
        solves[i] = sum(solve)
          
        for j in range(N):
            if i != j:
                for k in range(T):
                    if solve[k] == 1 and solved[j][k] == 0:
                        scores[i] += 1
                        
    for i, score in enumerate(scores):
        for j in range(N):
            if i != j:
                if scores[i] < scores[j]: grades[i] += 1
                elif scores[i] == scores[j]:
                    if solves[i] < solves[j]: grades[i] += 1
                    elif solves[i] == solves[j]:
                        grades[i] += i
    rank = [sorted(grades).index(grade) + 1 for grade in grades]
    
    print(f'#{t+1} {scores[P-1]} {rank[P-1]}')
    
        