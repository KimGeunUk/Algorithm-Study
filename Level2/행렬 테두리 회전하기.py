import copy
from shutil import move

# 시간 초과 - deepcopy 부분에서 시간 초과가 나타나는 것 같다.
def solution1(rows, columns, queries):
    answer = []
    
    box = [[(row-1)*columns + col for col in range(1, columns+1)] for row in range(1,rows+1)]
    tmp = copy.deepcopy(box)
    
    for i in queries:
        x1, y1, x2, y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        move_list = []
        
        for move_y in range(y1, y2+1):         
            if move_y == y2:
                tmp[x1+1][move_y] = box[x1][y2]
                move_list.append(box[x1][y2])
            else:
                tmp[x1][move_y+1] = box[x1][move_y]
                move_list.append(box[x1][move_y])
        for move_x in range(x1, x2+1):            
            if move_x == x2:
                tmp[x2][y2-1] = box[x2][y2]
                move_list.append(box[x2][y2])
            else:
                tmp[move_x+1][y2] = box[move_x][y2]
                move_list.append(box[move_x][y2])
        
        for move_y in range(y2-1, y1-1, -1):      
            if move_y == y1:
                tmp[x2-1][y1] = box[x2][y1]
                move_list.append(box[x2][y1])
            else:
                tmp[x2][move_y-1] = box[x2][move_y]
                move_list.append(box[x2][move_y])
        
        for move_x in range(x2-1, x1-1, -1):        
            if move_x == x1:
                pass
            else:
                tmp[move_x-1][y1] = box[move_x][y1]
                move_list.append(box[move_x][y1])
        
        box = copy.deepcopy(tmp)
        answer.append(min)
        
    return answer

# 한 번에 처리하여따 - 성공
def solution3(rows, columns, queries):
    answer = []    
    box = [[(row-1)*columns + col for col in range(1, columns+1)] for row in range(1,rows+1)]
    
    for i in queries:
        x1, y1, x2, y2 = i[0]-1, i[1]-1, i[2]-1, i[3]-1
        
        up = box[x1][y1:y2+1]
        right = [box[j][y2] for j in range(x1, x2+1)]
        down = list(reversed(box[x2][y1:y2+1]))
        left = list(reversed([box[j][y1] for j in range(x1, x2+1)]))
        
        # 부분을 뜯어서 한줄로 만들었다.
        move_list = up[:y2-y1]+right[:x2-x1]+down[:y2-y1]+left[:x2-x1]
        
        # 마지막 부분을 pop 한 뒤 처음에 넣고 끝을 알 수 있도록 다시 pop한 부분을 끝에 추가하였다.
        move_list.insert(0, move_list.pop())
        move_list.append(move_list[0])
       
        answer.append(min(move_list))
        
        # 뜯은 부분을 다시 조합하였다. 
        up = move_list[:y2-y1+1]
        right = move_list[y2-y1:y2-y1+1+x2-x1]
        down = move_list[y2-y1+x2-x1:y2-y1+1+x2-x1+y2-y1]
        left = move_list[y2-y1+x2-x1+y2-y1:y2-y1+1+x2-x1+y2-y1+x2-x1]
          
        box[x1][y1:y2+1] = up        
        for idx, j in enumerate(range(x1, x2+1)):
            box[j][y2] = right[idx]
        box[x2][y1:y2+1] = list(reversed(down))
        for idx, j in enumerate(range(x1, x2+1)):
            box[j][y1] = left[-idx-1]        
        
    return answer

# 다른사람 풀이
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))
    return answer
    
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))