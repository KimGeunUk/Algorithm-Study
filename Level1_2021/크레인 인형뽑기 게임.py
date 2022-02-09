#인형의 처음 상태는 문제에 주어진 예시와 같습니다.
#크레인이 [1, 5, 3, 5, 1, 2, 1, 4] 번 위치에서 
#차례대로 인형을 집어서 바구니에 옮겨 담은 후, 
#상태는 아래 그림과 같으며 바구니에 담는 과정에서 
#터트려져 사라진 인형은 4개 입니다.

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

answer = 0

room = 0
    
result=[]
    
for i in range(len(moves)):
    room = moves[i]
        
    for j in range(len(board)):
        if board[j][room-1] >= 1:
            result.append(board[j][room-1])

            if len(result) >= 2:            
                if result[-1] == result[-2]:
                    answer += 2                    
                    del result[-1]
                    del result[-1]                   

            board[j][room-1] = 0
            break

print(result)
print(answer)