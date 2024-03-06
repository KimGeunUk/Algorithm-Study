import sys
input = sys.stdin.readline

def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

e, f = (a * d + c * b), b * d

g = gcd(e, f)

print(int(e / g), int(f / g))