def DP(N):    
    DP_[1] = 1
    DP_[2] = 1    
    DP_[3] = 1
    
    for i in range(4, N+1):
        DP_[i] = DP_[i-2] + DP_[i-3]

    print(DP_[N])
    
T = int(input())

DP_ = [0] * 101

for _ in range(T):
    N = int(input())
    DP(N)