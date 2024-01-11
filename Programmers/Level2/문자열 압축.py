# 내 풀이
def kgw_solution(s):
    str_list = []
    if len(s) == 1:
        return 1

    for k in range(1, int(len(s)/2)+1):
        i = 0
        count = 1

        str1 = ''
        while i <= len(s)-k:                         # 5
            for j in range(i+k, len(s), k):         # 2, 8, 2
                if s[i:i+k] == s[j:j+k]:
                    count += 1
                    if j == len(s)-k:
                        if count == 1:
                            str1 += s[i:i+k]
                        else:
                            str1 += str(count) + s[i:i+k]
                        i = j
                        count = 1
                        break
                else:
                    if count == 1:
                        str1 += s[i:i+k]
                        count = 1
                        if j >= len(s) - k:
                            if count == 1:
                                str1 += s[j:j+k]
                            else:
                                str1 += str(count) + s[j:j+k]
                            i = j
                            count = 1
                            break
                    else:
                        str1 += str(count) + s[i:i+k]
                        count = 1
                        if j >= len(s) - k:
                            if count == 1:
                                str1 += s[j:j + k]
                            else:
                                str1 += str(count) + s[j:j+k]
                            i = j
                            count = 1
                            break
                    i = j
                    count = 1
                    break
            if i == len(s)-k:
                break
            print(str1)

        str_list.append(len(str1))
    return min(str_list)

# 모범 풀이     -----------------------------------------------------------------------------------------------------
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1

    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = ["aabbaccc"]

for x in a:
    print(solution(x))

# 모범 풀이     -----------------------------------------------------------------------------------------------------
def solution2(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    answer = len(s)
    for l in range(1, len(s) + 1):
        last = (0, "")
        temp = ""
        for i in range(0, len(s), l):
            t = s[i:i+l]
            if t == last[1]:
                last = (last[0] + 1, t)
            else:
                if last[0] != 0:
                    temp += "%d%s" % last if last[0] > 1 else last[1]
                last = (1, t)
        if last[0] > 0:
            temp += "%d%s" % last if last[0] > 1 else last[1]
        answer = min(answer , len(temp))
    return answer

# print(solution("a")) # 1
# print(solution("acacacbacacac")) # 9 # 3acba2cac
# print(solution("acacacacacacbacacacacacac")) #9
# print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # 4 # 100a
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))

