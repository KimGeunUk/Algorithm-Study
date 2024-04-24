T = int(input())

for t in range(T):
    s = input().strip()
        
    count = 0
    
    i = 0
    while i < len(s):
        if s[i] == '(':
            if i < len(s) - 1 and (s[i+1] == '|' or s[i+1] == ')'):
                count += 1
                i += 1
        elif s[i] == ')':
            if i >= 1 and (s[i-1] == '|' or s[i-1] == '('):
                count += 1
                i += 1
        i += 1
                
    print(f'#{t+1} {count}')