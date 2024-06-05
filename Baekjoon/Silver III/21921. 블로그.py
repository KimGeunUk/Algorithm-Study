N, X = map(int, input().split())
visited = list(map(int, input().split()))

sum_visited = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_visited[i] = visited[i-1] + sum_visited[i-1]

max_value = -1
max_count = 0

for i in range(1, N-X+2):
    value = sum_visited[i+X-1] - sum_visited[i-1]
    
    if value > max_value:
        max_value = value
        max_count = 1
    elif value == max_value:
        max_count += 1

if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(max_count)