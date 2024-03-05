import sys
input = sys.stdin.readline

n = int(input())

s = set()

for _ in range(n):
    info = input().strip().split()
    name, status = info[0], info[1]
    
    if status == "enter":
        s.add(name)
    elif status == "leave":
        s.remove(name)

names = sorted(list(s), reverse=True)

for name in names:
    print(name)