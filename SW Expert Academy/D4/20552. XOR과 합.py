T = int(input())

for t in range(T):
    X, S = map(int, input().split())
    bin_X = format(X, 'b')
    # if 2 ** (len(bin_X) - 1) > S:
    #     print(-1)
    #     break
    
    # if X == 0 and S == 0:
    #     print(0)
    #     break

    L = []
    
    for i in range(1, S-1):
        print((S-1) ^ i)
        print((S-1) ^ i ^ i)
        break
        temp = []        
        # while True:
        #     S -= i
        #     if S ^ i
        
    
    # 8 9
    # 1000 1 1