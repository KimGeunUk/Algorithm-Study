T = int(input())

for t in range(T):
    S = input().strip()
    
    D = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}
    
    print(f'#{t+1} {D[S]}')