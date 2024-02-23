import sys
input = sys.stdin.readline

answer = 0

n, b = input().split()

for idx, _n in enumerate(n[::-1]):
    if ord(_n) >= 65:
        answer += (ord(_n) - 55) * (int(b) ** idx)
    else:
        answer += int(_n) * (int(b) ** idx)

print(answer)