T = int(input())

for t in range(T):
    cards = {2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16, 11: 4}
    
    N = int(input())
    S = 0
    
    for _ in range(N):
        card = int(input())        
        S += card
        cards[card] -= 1
        
    mod = 21 - S
    
    A, B = 0, 0
    
    for key in cards.keys():
        if S + key <= 21:
            A += cards[key]
        else:
            B += cards[key]
    
    if A <= B: print(f'#{t+1} STOP')
    else: print(f'#{t+1} GAZUA')