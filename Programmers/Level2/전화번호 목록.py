def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book)
    
    pre = phone_book[0]
    for idx, i in enumerate(phone_book[1:]):
        l = len(pre)
        if i[:l] == pre:
            return False
        pre = i        
    
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))