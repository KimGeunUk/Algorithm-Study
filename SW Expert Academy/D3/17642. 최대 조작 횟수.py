T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    
    diff = b - a
    count = 0
    
    if diff == 0: print(f'#{i+1} 0')
    elif diff < 2:print(f'#{i+1} -1')
    elif diff % 2 == 0: print(f'#{i+1} {diff//2}')
    else: print(f'#{i+1} {(diff - 3)//2 + 1}')