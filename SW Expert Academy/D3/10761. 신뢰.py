T = int(input())

for t in range(T):
    S = input().split()
    
    N = int(S[0])
    orders = S[1:]
    
    B_now, B_count = 1, 0
    O_now, O_count = 1, 0
    
    prev_color = None
    B_can_move = 0
    O_can_move = 0
    
    for i in range(0, len(orders), 2):
        color, next = orders[i], int(orders[i+1])
        
        if color == 'B':
            if prev_color == 'O':
                min_val = 0 if B_now - B_can_move < 0 else B_now - B_can_move
                max_val = B_now + B_can_move
                
                if next in range(min_val, max_val + 1):
                    B_now = next
                else:
                    if next < min_val: B_now = min_val
                    elif next > max_val: B_now = max_val             
            
            if B_now == next:
                B_count += 1
                if prev_color != 'O':
                    O_can_move += 1
                else:
                    O_can_move = 1
            else:
                B_count += abs(B_now - next) + 1
                if prev_color != 'O':
                    O_can_move += abs(B_now - next) + 1
                else:
                    O_can_move = abs(B_now - next) + 1
                B_now = next
            
            prev_color = 'B'
                
        elif color == 'O':
            if prev_color == 'B':
                min_val = 0 if O_now - O_can_move < 0 else O_now - O_can_move
                max_val = O_now + O_can_move

                if next in range(min_val, max_val + 1):
                    O_now = next
                else:
                    if next < min_val: O_now = min_val
                    elif next > max_val: O_now = max_val                    
            
            if O_now == next:
                O_count += 1
                if prev_color != 'B':
                    B_can_move += 1
                else:
                    B_can_move = 1
            else:
                O_count += abs(O_now - next) + 1
                if prev_color != 'B':
                    B_can_move += abs(O_now - next) + 1
                else:
                    B_can_move = abs(O_now - next) + 1
                O_now = next
            
            prev_color = 'O'
        
    print(f'#{t+1} {B_count + O_count}')
                
                
    
    
    