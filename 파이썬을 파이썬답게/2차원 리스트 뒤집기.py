import copy
def solution(mylist):
    answer = copy.deepcopy(mylist)
    for i in range(len(mylist)):
        for j in range(len(mylist[0])):
            if i != j:
                answer[i][j] = mylist[j][i]                
    return answer

# zip
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
print(zip(*mylist))
print(new_list)

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))