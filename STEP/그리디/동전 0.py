import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

answer = 0
for c in coin[::-1]:
    if c <= K:
        answer += K // c
        K = K % c

print(answer)