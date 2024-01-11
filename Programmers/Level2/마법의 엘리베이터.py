def solution(storey):
    answer = 0

    while storey:
        mod = storey % 10
        
        if mod > 5:
            _add = 10 - mod
            storey += _add
            answer += _add            
        elif mod < 5:
            _sub = mod
            storey -= _sub
            answer += _sub
        else:
            mmod = storey % 100
            if mmod > 50:
                storey += mod
            else:
                storey -= mod
            answer += mod
        
        storey /= 10

    return int(answer)

print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(678)) # 8
print(solution(95)) # 7