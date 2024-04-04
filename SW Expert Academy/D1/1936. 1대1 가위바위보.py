a, b = map(int, input().split())

if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
elif (b == 1 and a == 2) or (b == 2 and a == 3) or (b == 3 and a == 1):
    print('A')
