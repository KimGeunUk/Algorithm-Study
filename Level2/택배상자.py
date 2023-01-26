from collections import deque

def solution(order):
    answer = 0
    
    main = deque([i for i in range(1, len(order)+1)])
    sub = deque()
    
    for o in order:
        if len(main) > 0 and o >= main[0]:
            while True:
                p = main.popleft()
                if p != o:
                    sub.appendleft(p)
                else:
                    answer += 1
                    break
        else:
            if sub[0] == o:
                sub.popleft()
                answer += 1
            else:
                break                
        
    return answer