T = int(input())

for t in range(T):
    N, D, G = map(int, input().split())
    
    win = int(N * (D / 100))
    lose = N - win