from collections import deque

def atoz(i: int):
    return (i - 97) % 26 + 97

def solution(s, skip, index):
    answer = ''

    for s_ in s:
        next_alpha = deque([ord(s_) + i for i in range(1, index+1)])
        count = index
        
        while True:
            if count == 0: break
            
            p = next_alpha.popleft()            
            if chr(atoz(p)) in skip:
                next_alpha.append(p + count)
            elif chr(atoz(p)) not in skip:
                count -= 1

        answer += chr(atoz(p))

    return answer

def solution(s, skip, index):
    answer = ''
    
    lower = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    
    for s_ in s:
        answer += lower[(lower.index(s_) + index) % len(lower)]

    return answer

print(solution("aukks", "wbqd", 5)) # happy
print(solution("yyyyy", "za", 2)) # ccccc
print(solution("zzzz", "abcd", 2)) # eeee