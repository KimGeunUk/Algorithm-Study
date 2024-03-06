import sys
input = sys.stdin.readline

def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b:
        a, b = b, a % b
    return a

n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))
    
diff = []
for i in range(n-1):
    diff.append(l[i+1] - l[i])

g = diff[0]
for i in diff[1:]:
    g = gcd(i, g)

length = int((max(l) - min(l)) / g) + 1
    
print(length)
print(length - len(l))

