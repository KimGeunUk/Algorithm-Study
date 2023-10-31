def solution(babbling):
    answer = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    for idx in range(len(babbling)):
        can = ["aya", "ye", "woo", "ma"]
        previous = ""
        while True:
            for c in can:
                if babbling[idx][:len(c)] == c and previous != c:
                    babbling[idx] = babbling[idx][len(c):]
                    previous = c
                    break
            else:
                break
            
            if babbling[idx] == "":
                answer += 1
                break
    
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))