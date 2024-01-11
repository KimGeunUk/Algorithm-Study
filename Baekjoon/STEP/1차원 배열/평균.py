N = int(input())
l = list(map(int, input().split()))
n = 0
for l_ in l:
    n += l_/max(l)*100
print(n/N)
