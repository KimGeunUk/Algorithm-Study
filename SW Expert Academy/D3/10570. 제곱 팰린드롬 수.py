T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    count = 0
    for i in range(A, B+1):
        sqrt = i ** 0.5
        if sqrt.is_integer():
            
            str_i = str(i)
            len_i = len(str_i)
            if len_i % 2 == 0:
                L = str_i[:(len_i-1)//2 + 1]
                R = str_i[(len_i-1)//2 + 1:]
            else:
                L = str_i[:(len_i-1)//2]
                R = str_i[(len_i-1)//2 + 1:]
                
                if L == R[::-1]:
                    
                    str_i = str(int(sqrt))
                    len_i = len(str_i)
                    if len_i % 2 == 0:
                        L = str_i[:(len_i-1)//2 + 1]
                        R = str_i[(len_i-1)//2 + 1:]
                    else:
                        L = str_i[:(len_i-1)//2]
                        R = str_i[(len_i-1)//2 + 1:]
                        
                    if L == R[::-1]: count += 1
                    
    print(f'#{t+1} {count}')