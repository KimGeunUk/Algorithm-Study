import sys
input = sys.stdin.readline

answer = ''

N, X = map(int, input().split())
l = list(map(int, input().split()))

for l_ in l:
    if X > l_:
        answer += str(l_) + ' '
        
print(answer)