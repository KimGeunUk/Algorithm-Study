import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n*2, 2):
    space = " " * (n - (i // 2 + 1))
    start = "*" * i
    print(space+start)
    
for i in range(n*2 - 3, -1, -2):
    space = " " * (n - (i // 2 + 1))
    start = "*" * i
    print(space+start)
    