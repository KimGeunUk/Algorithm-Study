def g(A):
    return A[::-1]

def f(A):
    lenA = len(A)
    b = bin(int(A, 2) ^ int('1'*lenA, 2))[2:]
    return '0'*(len(A)-len(b)) + b

T = int(input())

for t in range(T):
    K = int(input())
    
    for i in range(1, 1001):
        if K < 2 ** i:
            break
    
    S = '0'
        
    for _ in range(i - 1):
        S = S + '0' + f(g(S))

    print(f'#{t+1} {S[K-1]}')

T = int(input())

for t in range(T):
    K = int(input())
    K -= 1
    answer = 0
    
    while K > 0:
        if K % 2 == 1:
            K = (K-1)/2
        if K % 4 == 0:
            answer = 0
            break
        elif K % 2 == 0:
            answer = 1
            break
    
    print(f'#{t+1} {answer}')
    
    