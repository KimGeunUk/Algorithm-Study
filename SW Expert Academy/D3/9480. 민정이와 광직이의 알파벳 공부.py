from itertools import combinations

T = int(input())

for t in range(T):
    N = int(input())    
    words = [input().strip() for _ in range(N)]
    count = 0
    
    for i in range(1, N+1):
        for word in combinations(words, i):            
            S = set()
            for w in word:
                S |= set(w)
            if len(S) == 26:
                count += 1
    print(f'#{t+1} {count}')