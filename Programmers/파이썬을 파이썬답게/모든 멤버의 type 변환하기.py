
def solution(mylist):
    answer = []
    
    for i in mylist:
        answer.append(int(i))
    
    return answer

# map

list1 = ['1', '100', '33']
list2 = list(map(int, list1))

print(solution(['1', '100', '33']))