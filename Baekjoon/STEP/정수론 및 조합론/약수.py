import sys
input = sys.stdin.readline

N_len = int(input()) # N <= 50
N = list(map(int, input().split()))

N.sort()

print(N[0] * N[-1])