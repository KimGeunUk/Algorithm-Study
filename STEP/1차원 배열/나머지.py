l = list()
for _ in range(10):
    i = int(input()) % 42
    if i not in l:
        l.append(i)
print(len(l))