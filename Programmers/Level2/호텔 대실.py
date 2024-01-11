from collections import deque
def solution(book_time):
    room = []
    
    book_time = [[int(b[0][:2])*60+int(b[0][-2:]), int(b[1][:2])*60+int(b[1][-2:])] for b in book_time]    
    book_time = deque(sorted(book_time, key=lambda x: (x[0], x[1])))
    
    p = book_time.popleft()
    room.append(p)
    
    while book_time:
        p = book_time.popleft()
        
        rl = len(room)
        can_book = []
        
        for idx in range(rl):
            out_time = room[idx][1]+10
            in_time = p[0]
            if out_time <= in_time:
                can_book.append([idx, p, in_time-out_time])
   
        if can_book:
            can_book = sorted(can_book, key=lambda x: x[2])
            room[can_book[0][0]] = can_book[0][1]       
        else:
            room.append(p)

    return len(room)

# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3
print(solution([["08:00", "08:30"], ["08:00", "13:00"], ["12:30", "13:30"]]))