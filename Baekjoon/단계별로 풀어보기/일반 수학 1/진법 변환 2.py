import sys
input = sys.stdin.readline

answer = ''

n, b = map(int, input().strip().split())

while n:
    n, m = divmod(n, b)
    
    if m > 9:
        m += 55
        answer += chr(m)
    else:
        answer += str(m)

print(answer[::-1])