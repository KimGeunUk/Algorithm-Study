money = int(input())
n = int(input())
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += a * b
if s == money:
    print("Yes")
else:
    print("No")