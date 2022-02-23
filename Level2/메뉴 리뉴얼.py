import itertools as it

def solution(orders, course):
    answer = []
    result = []
    order_count = {}
    count_order = {}
    
    for i in course:
        for order in orders:
            order = sorted(order)
            if len(order) >= i:
                iter_n = it.combinations(order, i)
                for iter in iter_n:
                    if iter not in order_count:
                        order_count[iter] = 0
                    else:
                        order_count[iter] += 1
                        
        for key, value in order_count.items():
            if value not in count_order.keys():
                count_order[value] = [key]
            else:
                count_order[value] += [key]
                        
        if len(count_order) == 0:
            pass
        elif max(count_order.keys()) >= 1:
            result.append(count_order[max(count_order.keys())])
            
        order_count = {}
        count_order = {}
    
    for i in result:
        for j in i:
            answer.append(''.join((list(j))))
            
    answer = sorted(answer)
    
    return answer

# 다른사람 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))       # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))     # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))       # ["WX", "XY"]