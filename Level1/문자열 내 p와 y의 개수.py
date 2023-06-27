def solution(s):    
    
    countp=0
    county=0

    for i in range(len(s)):
        if s[i] == 'p' or s[i] =='P':
            countp += 1
        elif s[i] == 'y' or s[i] == 'Y':
            county += 1
    
    if countp == 0 and county ==0:
        return True
    else:
        if countp == county:
            return True
        else:
            return False

print(solution('pPoooyY'))
print(solution('Pyy'))
    
    