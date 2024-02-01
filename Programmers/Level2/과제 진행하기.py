def solution(plans):
    answer = []
    
    for plan in plans:
        plan[1] = int(plan[1][:2]) * 60 + int(plan[1][3:])
        
    plans = sorted(plans, key=lambda x: x[1])
    print(plans)
    
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