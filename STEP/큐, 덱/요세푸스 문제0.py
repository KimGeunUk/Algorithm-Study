from collections import deque

N, K = map(int, input().split())

josephus = deque([i for i in range(1, N+1)])
josephus.reverse()

answer = '<'
while len(josephus) > 0:
    josephus.rotate(K)
    answer += str(josephus.popleft()) + ', '
print(answer[:-2] + '>')