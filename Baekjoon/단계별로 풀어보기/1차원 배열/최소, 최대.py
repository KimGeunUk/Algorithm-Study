import sys
input = sys.stdin.readline

answer = ''

N = int(input())
l = list(map(int, input().split()))

print(min(l), max(l))