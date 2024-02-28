import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    sides = sorted([a, b, c])
    
    if a == b == c == 0: break    
    
    if a == b == c:
        print("Equilateral")
    elif (a == b or b == c or a == c) and (sides[2] < sum(sides[:2])):
        print("Isosceles")
    elif (a != b != c) and (sides[2] < sum(sides[:2])):
        print("Scalene")
    else:
        print("Invalid")
    