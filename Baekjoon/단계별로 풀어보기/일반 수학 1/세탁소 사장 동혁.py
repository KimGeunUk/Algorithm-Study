import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    c = int(input())
    
    q, c = divmod(c, 25)
    d, c = divmod(c, 10)
    n, c = divmod(c, 5)
    p, c = divmod(c, 1)

    print(f"{int(q)} {int(d)} {int(n)} {int(p)}")