N = input()
iN = int(N)

diff = len(N) * 9

answer = 0
for i in range(iN-diff, iN+diff+1):
    if i > 0:
        iL = list(map(int, str(i)))
        
        if i + sum(iL) == iN:
            answer = i
            break
print(answer)

# 속도 같음
# answer = []
# for i, j in zip(range(iN-1, iN-diff-1, -1), range(iN+1, iN+diff+1, 1)):
#     if i > 0:
#         iL = list(map(int, str(i)))        
        
#         if i + sum(iL) == iN:
#             answer.append(i)
            
#     jL = list(map(int, str(j)))
    
#     if j + sum(jL) == iN:
#         answer.append(j)
        

# print(0) if len(answer) == 0 else print(min(answer))

