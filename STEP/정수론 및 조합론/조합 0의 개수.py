# def fac(n):
#     answer = 1
#     for i in range(1, n+1):
#         answer *= i
#     return answer 

# def nCr(n, r):
#     return fac(n) // (fac(r) * fac(n-r))

# N, M = map(int, input().split())

# sN = nCr(N, M)

# answer = 0
# for n in range(10, sN, 10**2):
#     if n != '0':
#         break    
#     answer += 1
    
# print(answer)

# 5가 몇번 나누어지는지 
def fiveCount(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

# 2가 몇번 나누어지는지
def twoCount(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

n, m = map(int, input().split())

if m == 0:
    print(0)
else:
    # 2와 5의 개수를 nCm을 구할 때처럼 구해서 더 작은 개수를 선택한다.
    print(min(twoCount(n) - twoCount(m) - twoCount(n - m), fiveCount(n) - fiveCount(m) - fiveCount(n - m)))