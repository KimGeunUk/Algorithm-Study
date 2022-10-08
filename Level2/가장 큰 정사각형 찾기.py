""" 
문제 설명
1와 0로 채워진 표(board)가 있습니다. 
표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

예를 들어
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0
가 있다면 가장 큰 정사각형은

1	1	1
1	1	1
1	1	1

가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

제한사항
표(board)는 2차원 배열로 주어집니다.
표(board)의 행(row)의 크기 : 1,000 이하의 자연수
표(board)의 열(column)의 크기 : 1,000 이하의 자연수
표(board)의 값은 1또는 0으로만 이루어져 있습니다.
"""

from collections import deque
def solution(board):
    answer = []

    dx = [1, 0, 1]
    dy = [0, 1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
                        
        count = 0
        while queue:
            x, y = queue.popleft()
            
            if board[x][y] == 1:
                
                for i in range(3):                    
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if nx >= len(board) or ny >= len(board[0]): continue
                    
                    if board[nx][ny] == 0: break
                    
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
                    
                if i == 2 and board[nx][ny] == 1:
                    count+=1
                else:
                    break                

        return count
    
    print(bfs(0,1))
    
    return answer

print(solution([[0,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [0,1,1,0]])) # 9

print(solution([[0,0,1,1],
                [1,1,1,1]])) # 4