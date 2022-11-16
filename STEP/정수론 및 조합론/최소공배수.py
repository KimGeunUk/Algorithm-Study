def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    a, b = min(a, b), max(a, b)
    return (a * b) // gcd(a, b)

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))