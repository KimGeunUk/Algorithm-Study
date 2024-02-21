# import sys
# input = sys.stdin.readline

# def dfs(LIST, IDX_LIST):
#     global max_, min_
        
#     if len(LIST) == N-1:
#         cal = A[0]
        
#         for num, op in zip(A[1:], LIST):
#             if op == '+':
#                 cal += num
#             elif op == '-':
#                 cal -= num
#             elif op == '*':
#                 cal *= num
#             elif op == '/':
#                 if cal < 0:
#                     cal = -(abs(cal) // num)
#                 else:
#                     cal //= num
            
#         if min_ > cal:
#             min_ = cal
        
#         if max_ < cal:
#             max_ = cal

#         return
    
#     for idx, o in enumerate(op_list):
#         if idx not in IDX_LIST:
#             LIST.append(o)
#             IDX_LIST.append(idx)
#             dfs(LIST, IDX_LIST)
#             LIST.pop()
#             IDX_LIST.pop() 


# N = int(input())
# A = list(map(int, input().split()))
# op = list(map(int, input().split())) # + - * /

# max_ = -float('inf')
# min_ = float('inf')

# op_list = list()
# for i in range(op[0]):
#     op_list.append('+')
# for i in range(op[1]):
#     op_list.append('-')
# for i in range(op[2]):
#     op_list.append('*')
# for i in range(op[3]):
#     op_list.append('/')
    
# dfs([], [])

# print(max_, min_)

def dfs(idx, cal):    
    global max_, min_
    
    if idx == N:
        max_ = max(max_, cal)
        min_ = min(min_, cal)
        return
    
    for i in range(4):
        tmp = cal
        if op[i] > 0:
            if i == 0:
                cal += A[idx]
            elif i == 1:
                cal -= A[idx]
            elif i == 2:
                cal *= A[idx]
            else:
                cal = int(cal/A[idx])
            
            op[i] -= 1            
            dfs(idx+1, cal)            
            op[i] += 1
            
            cal = tmp # 이전 값 기억

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * /

max_ = -float('inf')
min_ = float('inf')

dfs(1, A[0])

print(max_)
print(min_)