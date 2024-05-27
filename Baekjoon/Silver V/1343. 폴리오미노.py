board = input().strip()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board: print('-1')
else: print(board)


"""
board = input().strip()
board += '.'

i = 0
count = 0
answer = ''

while True:
    if board[i] == 'X': count += 1
    elif board[i] == '.':
        answer += '.'
        count = 0
    
    if i == len(board) - 1: break
    
    if (board[i] == 'X' and board[i+1] == '.'):
        div, mod = divmod(count, 4)
        if mod == 0:
            answer += 'AAAA' * div
        elif mod == 2:
            answer += 'AAAA' * div
            answer += 'BB'
        else:
            answer = '-1.'
            break
    
    i += 1

print(answer[:-1])
"""