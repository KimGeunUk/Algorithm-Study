import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
sides = sorted([a, b, c])

print(sides[0] + sides[1] + min(sides[2], sides[0] + sides[1] - 1))