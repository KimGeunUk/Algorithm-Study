def solution(mylist):
    answer = ''    
    for i in mylist:
        answer += i
    return answer

# join
my_list = ['1', '100', '33']
answer = ''.join(my_list)

print(solution(['1', '100', '33']))