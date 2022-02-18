a = [1, 2, 3, 4, 0, 5, 6]
i = a.index(min(a[2:]))
print(i)
print(a[2:3] + a[4:])

b = [1,1,[1,1]]
if [1, 1] in b:
    print('Y')
print(sum(a))