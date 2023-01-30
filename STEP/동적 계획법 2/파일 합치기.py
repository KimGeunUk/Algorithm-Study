import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())    
    files = [0] + list(map(int, input().split())) 

    # 누적합
    S = [0 for _ in range(K+1)]
    for i in range(1, K+1):
        S[i] = S[i-1] + files[i]
        
    # DP[i][j] : i에서 j까지 합치는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(files[i] ~ files[j])
    DP = [[0]*(K+1) for _ in range(K+1)]
    for i in range(2, K+1): # 부분 파일의 길이
        for j in range(1, K+2-i):   # 시작점
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
 
    print(DP[1][K])