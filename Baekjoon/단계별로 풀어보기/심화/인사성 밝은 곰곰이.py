import sys
input = sys.stdin.readline

n = int(input())

_sum = 0
s = set()

for _ in range(n):
    user = input().strip()
    
    if user == 'ENTER':
        _sum += len(s)       
        s = set()                
    else:
        s.add(user)

print(_sum + len(s))