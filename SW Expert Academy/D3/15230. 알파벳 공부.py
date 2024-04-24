T = int(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for t in range(T):
    letter = input().strip()
    
    # count = len(alphabet) - len(letter)
    count = 0
    
    for let, alpha in zip(letter, alphabet):
        if let == alpha:
            count += 1
        else:
            break
            
    print(f'#{t+1} {count}')