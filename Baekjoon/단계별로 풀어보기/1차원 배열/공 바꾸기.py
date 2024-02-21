import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())

    basket[i], basket[j] = basket[j], basket[i]
    
print(" ".join(map(str, basket[1:])))