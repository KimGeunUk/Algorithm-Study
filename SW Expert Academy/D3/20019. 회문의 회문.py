T = int(input())

for i in range(T):
    string = input().strip()
    
    N = len(string)
    if N % 2 != 0:
        A = string[:(N-1)//2]
        B = string[(N-1)//2 + 1:]
    else:
        A = string[:(N-1)//2 + 1]
        B = string[(N-1)//2 + 1:]
    
    if A == B[::-1]:
        N_A = len(A)
        if N_A % 2 != 0:
            a1 = A[:(N_A-1)//2]
            a2 = A[(N_A-1)//2 + 1:]
        else:
            a1 = A[:(N_A-1)//2 + 1]
            a2 = A[(N_A-1)//2 + 1:]
        
        N_B = len(B)
        if N_B % 2 != 0:
            b1 = B[:(N_B-1)//2]
            b2 = B[(N_B-1)//2 + 1:]
        else:
            b1 = B[:(N_B-1)//2 + 1]
            b2 = B[(N_B-1)//2 + 1:]
        
        if a1 == a2[::-1] and b1 == b2[::-1]:
            print(f'#{i+1} YES')
        else:
            print(f'#{i+1} NO')
    else:
        print(f'#{i+1} NO')