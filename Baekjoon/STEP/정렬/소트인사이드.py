N = list(input())
for i in range(len(N)-1):
    for j in range(i+1, len(N)):
        if N[i] < N[j]:
            N[i], N[j] = N[j], N[i]
print(''.join(N))