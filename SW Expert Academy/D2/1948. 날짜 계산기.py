T = int(input())

month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for i in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    
    if m1 == m2: print(f'#{i+1} {d2 - d1 + 1}')
    else:
        day = month_day[m1] - d1 + 1
        day += d2
        
        for m in range(m1 + 1, m2):
            day += month_day[m]
        
        print(f'#{i+1} {day}')
    