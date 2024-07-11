# import sys
# input = sys.stdin.readline

# N, score, P = map(int, input().split())

# if N > 0:
#     scores = list(map(int, input().split()))
    
#     answer = -1
#     answer_idx = -1
#     trigger = False
    
#     rank = 0
#     rank_temp = 0
#     before_score = float('inf')
    
#     for idx, sc in enumerate(scores):
#         if sc < before_score:
#             rank += rank_temp + 1
#             rank_temp = 0
#             before_score = sc
#         elif sc == before_score:
#             rank_temp += 1

#         if score >= sc:
#             if trigger == False:
#                 answer = rank
#                 trigger = True
                
#             if score == sc:
#                 answer_idx = rank + rank_temp + 1
#     else:
#         if trigger == False:
#             answer = rank + rank_temp + 1

#     if answer_idx > P or answer > P:
#         print(-1)
#     else:
#         print(answer)
# else:
#     print(1)

import sys
input = sys.stdin.readline

N, score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    
    if N == P and score <= scores[-1]:
        print(-1)
    else:
        rank = 1
        for s in scores:
            if s > score:
                rank += 1
            else:
                break
        
        if rank <= P:
            print(rank)
        else:
            print(-1)