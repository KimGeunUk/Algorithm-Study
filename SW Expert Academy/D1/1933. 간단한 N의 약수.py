N = int(input())
L = set()

for i in range(1, int(N ** 1/2)):
    if N % i == 0:
        L.add(i)
        L.add(N//i)

print(' '.join(map(str, sorted(list(L)))))