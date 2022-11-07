N = int(input())
for i in range(N):
    R, S = input().split()
    
    answer = ''
    for j in S:
        for _ in range(int(R)):
            answer += j
    print(answer)