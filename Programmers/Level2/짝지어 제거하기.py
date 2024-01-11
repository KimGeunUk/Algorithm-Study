import re

def solution(s):
    tmp = list()

    for i in s:
        if not tmp:
            tmp.append(i)
        elif tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)

    if len(tmp) == 0:
        return 1
    else:
        return 0

    # replace, sub, remove 들은 문장을 한번 읽고 처리해서 시간오류 !!!

    # count = 0
    # while count != len(s) - 1:
    #     if str[count] == str[count + 1]:
    #         # s = re.sub(s[count] + s[count], '', s)
    #         # s = s.replace('(([a-z])\\2)', '')
    #         str.remove(str[count])
    #         str.remove(str[count])
    #         print(str)
    #         count = 0
    #     else:
    #         count += 1
    #
    #     if len(str) == 0:
    #         return 1
    #
    # return 0

print(solution("baabaa"))
print(solution("cdcd"))

