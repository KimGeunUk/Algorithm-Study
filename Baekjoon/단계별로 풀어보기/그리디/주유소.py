N = int(input())

l = list(map(int, input().split())) + [0]
r = list(map(int, input().split())) + [0]

answer = 0
idx = 0

for i in range(1, N+1):    
    if r[idx] >= r[i]:
        answer += r[idx] * sum(l[idx:i])
        idx = i

print(answer)
