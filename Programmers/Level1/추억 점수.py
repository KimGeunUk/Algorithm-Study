def solution(name, yearning, photo):
    answer = []
    
    D = dict()
    for key, value in zip(name, yearning):
        D[key] = value
    
    for pt in photo:
        s = 0
        for p in pt:
            if p not in D.keys():
                D[p] = 0
            s += D[p]
        answer.append(s)
            
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])) # [19, 15, 6]
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])) # [67, 0, 55]
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]])) # [5, 15, 0]