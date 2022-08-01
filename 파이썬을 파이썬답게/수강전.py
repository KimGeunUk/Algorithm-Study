# 비효율적
def solution(mylist):
    answer = []
    for i in range(len(mylist)):
        n = len(mylist[i])
        answer.append(n)
        
    return answer

# 목표
def solution(mylist):
    return list(map(len, mylist))


print(solution([[1], [2]]))
print(solution([[1, 2], [3, 4], [5]]))