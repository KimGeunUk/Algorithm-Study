def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a

N = int(input())

R = list(map(int, input().split()))

for r in R[1:]:
    a, b = R[0], r
    g = gcd(a, b)
    print(f"{a // g}/{ b // g}")