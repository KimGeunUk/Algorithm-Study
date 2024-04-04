T = int(input())

day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for i in range(1, T + 1):
    numbers = input().strip()
    
    if (not 1 <= int(numbers[4:6]) <= 12):
        print(f'#{i} -1')
    elif (not 1 <= int(numbers[6:]) <= day[int(numbers[4:6])]):
        print(f'#{i} -1')
    else:
        print(f'#{i} {numbers[:4]}/{numbers[4:6]}/{numbers[6:]}')
