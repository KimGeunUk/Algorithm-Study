def solution(s):
    answer = ''
    num_dic = {"zero":0, "one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    j = 0
    for i, nums in enumerate(s):        
        if nums.isnumeric() == True:
            answer += str(nums)
            j=i+1
        elif s[j:i+1] in num_dic.keys():
            answer += str(num_dic[s[j:i+1]])
            j=i+1
            
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

# 나는 바보인가 보다.. ㅋㅋㅋㅋ
# 다른 사람 풀이 
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)