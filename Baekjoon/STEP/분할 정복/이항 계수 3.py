import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

# 팩토리얼
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

# 거듭제곱 계산(나머지 연산 적용)
def power(a, b):
    if b == 0:
        return 1
    if b % 2:    #홀수이면
        return (power(a, b//2) ** 2 * a) % p
    else:    #짝수이면
        return (power(a, b//2) ** 2) % p

top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(top * power(bot, p-2) % p)