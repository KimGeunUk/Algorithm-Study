from itertools import combinations as c

def gen_combinations(arr, n):
    result =[]
    max_result = -1
    
    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1):            
            result.append([elem]+C) 
            
            print([elem]+C)            
        
    return result

print(gen_combinations(range(5), 2))

def solution(cost, x):
    answer = []
    n = len(cost)
    for i in range(n, 0,-1):
        combi = list(c(range(n), i))        
        
        for c_ in combi:
            remain = x
            s = 0
            
            for c__ in c_:
                remain -= cost[c__]
                if remain < 0:
                    break
            else:
                for c__ in c_:
                    s += 2 ** c__
                answer.append(s)

                
#     return answer

print(solution([10, 20, 14, 40, 50, 10, 10, 10, 10, 10], 70))
print(solution([3, 4, 1], 8))