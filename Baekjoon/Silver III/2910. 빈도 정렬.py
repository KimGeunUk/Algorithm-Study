import sys
input = sys.stdin.readline

from collections import defaultdict

N, C = map(int, input().split())

numbers = list(map(int, input().split()))

D = defaultdict(int)

for number in numbers:
    D[number] += 1
    
items = sorted(list(D.items()), key=lambda x: -x[1])

for key, value in items:
    for _ in range(value):
        print(key, end=' ')
print()