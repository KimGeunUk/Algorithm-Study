# 중복 조합 풀이
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max = -float('inf')    
    
    c = list(combinations_with_replacement(range(0, 11), n))
    
    for c_ in c:
        lion_info = [0 for _ in range(11)]
        apeach, lion = 0, 0
        
        for score in c_:
            lion_info[10-score] += 1
            
        for score, (a, l) in enumerate(zip(info, lion_info)):
            if a == l == 0:
                continue
            elif a >= l:
                apeach += (10 - score)
            else:
                lion += (10 - score)
        
        if lion > apeach:
            gap = lion - apeach
            if gap > max:
                max = gap
                answer = lion_info
    
    return answer

# DFS 풀이
from copy import deepcopy
def dfs(a_s, l_s, cnt, idx, board, info, n):
    global max_diff, max_board
    # 화살 없는 경우
    if cnt > n:
        return
    
    # 과녁 점수 이상인 경우
    if idx > 10:
        diff = l_s - a_s
        if diff == max_diff:
            for i, j in zip(board[::-1], max_board[::-1]):
                if i < j:
                    break
                elif i > j:
                    max_board = board
                    break
        if diff > max_diff:
            board[10] = n - cnt
            max_board = board
            max_diff = diff
        
        return

    # 현재 어피치 상황
    now = info[idx]
    
    # 라이언이 선택할 수 있는 옵션 두가지
    # 0 -> 선택 x, now+1 -> 어피치보다 한발 더 맞추기
    for i in [now+1, 0]:
        board2 = deepcopy(board)
        
        if i == now+1:
            board2[idx] = now+1
            dfs(a_s, l_s+(10-idx), cnt+(now+1), idx+1, board2, info, n)
        else:
            if info[idx] > 0:
                dfs(a_s+(10-idx), l_s, cnt, idx+1, board2, info, n)
            else:
                dfs(a_s, l_s, cnt, idx+1, board2, info, n)

def solution(n, info):
    global max_diff, max_board
    answer = []
    
    max_diff = -float('inf')
    max_board = []
    board = [0 for _ in range(11)]
    
    dfs(0, 0, 0, 0, board, info, n)
    
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0])) # [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1])) # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # [1,1,1,1,1,1,1,1,0,0,2]
