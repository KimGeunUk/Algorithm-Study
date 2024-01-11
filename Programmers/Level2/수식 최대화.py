import itertools
import re
import copy

def solution(expression):
    oper = {'+': [], '-': [], '*': []}
    oper_v = {}
    operator = []
    operator_list = []    
    
    result = []
    
    expression_split = re.split(r'[\+\-\*]', expression)
    
    count = 0
    for i in expression:
        if i.isdigit() == False:
            if i not in operator:
                operator.append(i)
            oper[i].append(count)
            oper_v[count] = i
            count += 1
    
    for i in itertools.permutations(operator):
        operator_list.append(i)    

    order_list = []    
    for i in operator_list:
        tmp = []        
        for j in i:
            tmp += oper[j]
        order_list.append(tmp)
    
    for i in order_list:
        exp = copy.deepcopy(expression_split)
        count = 0        
        idx = 0
        where = copy.deepcopy(i)
        
        while True:
            if len(exp) == 1:                
                break
            
            cal = exp[where[idx]] + oper_v[i[idx]] + exp[where[idx] + 1]
            value = eval(cal)
            
            exp.pop(where[idx])
            exp[where[idx]] = str(value)            
            
            for l, k in enumerate(where[idx+1:]):
                if k > where[idx]:
                    where[l+idx+1] -= 1
            
            idx += 1 
                       
        result.append(abs(int(exp[0])))

    return max(result)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))