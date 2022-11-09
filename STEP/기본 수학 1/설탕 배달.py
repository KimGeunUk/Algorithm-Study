N = int(input())

i = 0
answer = []
while True:
    if (N - (5 * i)) % 3 == 0:
        print(i)
        answer.append(i + ((N - (5 * i)) // 3))
    elif (N - (3 * i)) % 5 == 0:
        print(i)
        answer.append(i + ((N - (3 * i)) // 5))

    
    i += 1    
    
    if (N - (5 * i)) < 0 or (N - (3 * i)) < 0:
        break
    
print(answer)
# 시간 초과
# answer = []
# 
# def dfs(n, s):    
#     if n < 0: return
#     elif n == 0:
#         answer.append(s)
#         return

#     dfs(n-5, s+1)
#     dfs(n-3, s+1)
    
# s = 0
# dfs(N, s)

# if len(answer) == 0: print(-1)
# else: print(min(answer))