import sys
input = sys.stdin.readline

n = int(input())

user = {"ChongChong"}

for _ in range(n):
    a, b = input().strip().split()
    
    if a in user:
        user.add(b)

    if b in user:
        user.add(a)
        
print(len(user))