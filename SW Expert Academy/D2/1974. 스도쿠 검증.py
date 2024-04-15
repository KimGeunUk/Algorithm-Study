T = int(input())

for i in range(1, T + 1):
    maps = [list(map(int, input().split())) for _ in range(9)]
    
    A = [set() for _ in range(9)]
    B = [set() for _ in range(9)]
    C = [set() for _ in range(9)]
    
    for row, r in enumerate(maps):
        for col, c in enumerate(r):
            A[row].add(c)
            B[col].add(c)
            C[((row // 3) * 3) + (col // 3)].add(c)
    
    for a, b, c in zip(A, B, C):
        if len(a) != 9 or len(b) != 9 or len(c) != 9:
            print(f'#{i} 0')
            break
    else:
        print(f'#{i} 1')