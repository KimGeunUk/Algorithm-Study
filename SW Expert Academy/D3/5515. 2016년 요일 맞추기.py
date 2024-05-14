D = {1: 31, 2: 29, 3:31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11:30, 12: 31}
M = {1: 4}

start = 4
for i in range(2, 13):
    v = (start + D[i-1] % 7) % 7
    M[i] = v
    start = v

T = int(input())

for t in range(T):
    m, d = map(int, input().split())
    
    print(f'#{t+1} {(M[m] + (d-1)%7)%7}')
    