def solution(s):
    i = 0

    while i < len(s):
        if 'one' in s:
            s = s.replace('one', str(1))
        elif 'two' in s:
            s = s.replace('two', str(2))
        elif 'three' in s:
            s = s.replace('three', str(3))
        elif 'four' in s:
            s = s.replace('four', str(4))
        elif 'five' in s:
            s = s.replace('five', str(5))
        elif 'six' in s:
            s = s.replace('six', str(6))
        elif 'seven' in s:
            s = s.replace('seven', str(7))
        elif 'eight' in s:
            s = s.replace('eight', str(8))
        elif 'nine' in s:
            s = s.replace('nine', str(9))
        elif 'zero' in s:
            s = s.replace('zero', str(0))
        i += 1

    return int(s)



print(solution("one4seveneight"))
# print(solution("23four5six7"))
# print(solution("2three45sixseven"))
# print(solution("123"))