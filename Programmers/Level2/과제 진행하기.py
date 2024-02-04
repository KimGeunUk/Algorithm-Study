def solution(plans):
    answer = []
    
    for plan in plans:
        plan[1] = int(plan[1][:2]) * 60 + int(plan[1][3:])
        plan[2] = int(plan[2])
        
    plans = sorted(plans, key=lambda x: x[1])[::-1]
    stop = []

    before = plans.pop()
    after = plans.pop()
    
    a = before
    b = after
    
    now_time = before[1]
    state = None
    
    while True:
        if plans == [] and stop == []:
            # print(a, b , after, before)
            # if (a != None) and (before[1] < after[1]) and (before[1] + before[2] > after[1]):
            #     answer.extend([after[0], before[0]])
            # else:
            answer.extend([before[0], after[0]])
                
            break
        
        if (a == None) or (now_time + before[2] <= after[1]):
            answer.append(before[0])
            now_time += now_time + before[2]
            
            state = "done"
        
        elif before[1] + before[2] > after[1]:            
            before[2] = before[2] - (after[1] - before[1])
            now_time = after[1]
            before[1] = now_time
            stop.append(before)
            
            state = "remain"

        a, b = None, None
                
        if plans:
            a = plans.pop()
        if stop:
            b = stop.pop()
            b[1] = now_time
        
        if state == "done":
            if a != None and b != None:
                if a[1] >= now_time + b[2]:
                    if after[1] >= now_time + b[2]:
                        b[1] = now_time
                        before = b
                        plans.append(a)
                    else:
                        stop.append(b)
                        before = after
                        after = a
                else:
                    before = after
                    after = a
                    stop.append(b)
            elif a == None and b != None:
                if after[1] >= b[1] + b[2]:
                    before = b
                else:
                    before = after
                    after = b
            elif a != None and b == None:
                before = after
                after = a
   
        elif state == "remain":
            before = after
                                
            if a == None:
                after = b
            else:
                after = a
                if b != None:
                    stop.append(b)
    
    return answer

print(solution([["korean", "11:40", "30"], 
                ["english", "12:10", "20"], 
                ["math", "12:30", "40"]])) # ["korean", "english", "math"]

print(solution([["science", "12:40", "50"], 
                ["music", "12:20", "40"], 
                ["history", "14:00", "30"], 
                ["computer", "12:30", "100"]])) # ["science", "history", "computer", "music"]

print(solution([["aaa", "12:00", "20"], 
                ["bbb", "12:10", "30"], 
                ["ccc", "12:40", "10"]])) # ["bbb", "ccc", "aaa"]

print(solution([["a","09:00","30"],
                ["b","09:10","20"],
                ["c","09:15","20"],
                ["d","09:55","10"],
                ["e","10:50","5"]])) # ["c","b","d","a","e"]

print(solution([["a", "09:00", "10"], 
                ["b", "09:10", "10"], 
                ["c", "09:15", "10"], 
                ["d", "09:30", "10"], 
                ["e", "09:35", "10"]])) # ["a", "c", "b", "e", "d"]

print(solution([["1", "00:00", "30"], 
                ["2", "00:10", "40"], 
                ["3", "00:20", "10"], 
                ["4", "00:25", "10"], 
                ["5", "01:10", "10"]])) # ["4", "3", "2", "5", "1"]

print(solution([["a","09:00","30"],
                ["b","09:10","20"],
                ["c","09:15","20"],
                ["d","09:55","10"],
                ["e","10:50","5"]])) # ["c","b","d","a","e"]