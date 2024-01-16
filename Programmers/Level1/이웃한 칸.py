def solution(board, h, w):
    n = len(board)
    count = 0
    color = board[h][w]
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if (h_check >= 0 and h_check < n) and (w_check >= 0 and w_check < n):
            if board[h_check][w_check] == color:
                count += 1

    return count

print(solution([["blue", "red", "orange", "red"], 
                ["red", "red", "blue", "orange"], 
                ["blue", "orange", "red", "red"], 
                ["orange", "orange", "red", "blue"]], 1, 1)) # 2

print(solution([["yellow", "green", "blue"], 
                ["blue", "green", "yellow"], 
                ["yellow", "blue", "blue"]], 0, 1)) # 1