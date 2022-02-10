def solution(new_id):    
    temp_id = []
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i, id in enumerate(new_id):
        if id.isalnum() == True or id == "-" or id == "_" or id == ".":
            temp_id.append(id)
            
    if temp_id == []:
        pass
    else:
        new_id = ''.join(temp_id)
        temp_id = []
    
    # 3단계      
    for i in range(len(new_id)):
        if new_id[-1] == '.' and i == len(new_id)-1:
            break
        if new_id[i]=='.' and new_id[i+1]=='.':
            pass
        else:
            temp_id.append(new_id[i])
    
    if len(temp_id) == 0:
        new_id = 'a'
        temp_id = []
    else:
        new_id = ''.join(temp_id)
        temp_id = []
    
    # 4단계    
    if new_id[0] == '.':
        temp_id = new_id[1:]
    elif new_id[-1] == '.':
        temp_id = new_id[:-1]
        
    if temp_id == []:
        pass
    else:
        new_id = ''.join(temp_id)
        temp_id = []
    
    # 5단계
    if len(new_id) == 0:
        new_id += 'a'
    
    # 6단계
    if len(new_id) >= 16:
        if new_id[14] == '.':
            temp_id = new_id[:14]
        else:
            temp_id = new_id[:15]
    # 7단계       
    if len(new_id) <= 2:
        temp_id.append(new_id)
        for i in range(3-len(new_id)):
            temp_id.append(new_id[-1])
            
    if temp_id == []:
        pass
    else:
        new_id = ''.join(temp_id)
        temp_id = []
        
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("./././././abcd/././././."))
print(solution("........................"))