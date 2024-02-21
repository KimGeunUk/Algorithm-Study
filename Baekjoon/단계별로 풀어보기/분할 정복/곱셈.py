import sys
input = sys.stdin.readline

# 거듭제곱 계산(나머지 연산 적용)
def power(a, b, c):
    if b == 0:
        return 1
    if b % 2:    #홀수이면
        return (power(a, b//2, c) ** 2 * a) % c
    else:    #짝수이면
        return (power(a, b//2, c) ** 2) % c

A, B, C = map(int, input().split())

print(power(A, B, C))