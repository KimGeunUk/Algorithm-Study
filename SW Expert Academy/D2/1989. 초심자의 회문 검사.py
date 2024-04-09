T = int(input())

for i in range(1, T + 1):
    s = input().strip()
    if len(s) % 2 != 0:
        mid = len(s) // 2
    
        if s[:mid] == s[mid+1:][::-1]:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
        
    else:
        mid = len(s) // 2
        print(s[:mid], s[mid:][::-1])
        if s[:mid] == s[mid:][::-1]:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
        