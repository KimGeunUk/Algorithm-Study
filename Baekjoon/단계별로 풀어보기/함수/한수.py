N = int(input())

c = 0
for i in range(1, N+1):
    str_i = str(i)
    
    if i < 100:
        c += 1
    else:
        s_1 = str_i[0]
        s_2 = str_i[1]
        
        diff = int(s_1) - int(s_2)        
           
        for idx, j in enumerate(str_i[2:], start=1):
            s_1 = str_i[idx]
            s_2 = j
            if int(s_1) - int(s_2) != diff:
                break
        else:
            c += 1
    
print(c)

# N = int(input())

# c = 0
# for i in range(1, N+1):
#     str_i = str(i)
    
#     if i < 100:
#         c += 1
#     elif int(str_i[0])-int(str_i[1]) == int(str_i[1]) - int(str_i[2]):
#         c += 1
    
# print(c)