def solution(strings, n):
    answer = []

    new_list = []

    _list = []

    strings.sort()

    for i in range(len(strings)):
        new_list.append(strings[i][n])
    
    new_list.sort()

    for i in new_list:
        for j in range(len(new_list)):
            if i == strings[j][n]:
                _list.append(strings[j])
                strings[j]='0'*100       
    
    print(new_list)
    print(_list)

    return answer

def solution2(strings, n):
    answer =[]

    answer = sorted(strings, key = (lambda x: x[n] + x))

    return answer

print(solution2(['sun', 'bed', 'car'],1))
print(solution2(['abce', 'abcd', 'cdx'],2))