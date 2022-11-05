import sys
input = sys.stdin.readline

r = int(input())
l = list()

for i in range(r):
    a, b = map(int, input().split())
    print(a+b)