from collections import defaultdict

def solution(gems):
    answer = []

    len_gems = len(gems)
    len_set_gems = len(set(gems))

    dd = defaultdict(int)

    start = 0
    end = len_set_gems
    
    for i in range(len_set_gems):
        dd[gems[i]] += 1
        
    while True:
        if len(dd) < len_set_gems:
            if end < len_gems:
                end += 1
                dd[gems[end-1]] += 1
            else:
                break
        else:
            dd[gems[start]] -= 1
            if dd[gems[start]] == 0:
                del dd[gems[start]]
                
            start += 1

            if len(dd) < len_set_gems:
                if answer == []:
                    answer = [start, end]
                else:
                    if answer[1] - answer[0] > end - start:
                        answer = [start, end]

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]