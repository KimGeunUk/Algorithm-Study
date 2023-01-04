import sys
input = sys.stdin.readline

N, B = map(int, input().split())

A = [[*map(int, input().split())] for _ in range(N)]

def power(A, B):
    N = len(A)
    answer = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            s = 0
            for a, b in zip(A[r], B[:]):
                s += a * b[c]
            answer[r][c] = s % 1000
     
    return answer

def div_power(A, B):
    if B == 1:
        N = len(A)
        for x in range(N):
            for y in range(N):
                A[x][y] %= 1000
        return A
    
    T = div_power(A, B//2)
    if B % 2:
        return power(power(T, T), A)
    else:
        return power(T, T)

answer = div_power(A, B)

for a in answer:
    print(*a)