import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

L.sort()

answer = 0
for i in range(1, len(L)+1):
    answer += sum(L[:i])
print(answer)