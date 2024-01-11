import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
f = int(input())

print(l.count(f))